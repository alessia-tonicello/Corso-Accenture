from __future__ import annotations
import numpy as np
from dataclasses import dataclass
import re
from typing import Any, Dict, List, Optional, Tuple

# il @dataclass crea il modello dati come il record pulito deve essere formato
@dataclass
class CleanRecord:
    age: int
    income: float
    debts: int
    credit_score: int
    approved: int

# classe per Parsing/sanificazione, deve convertire campi grezzi in numeri gestendo formati strani
#non è il parser a decidere se il record è valido, ma il parser si liimita a convertire e se non può resituisce None
class FieldParser:
    def parse_int(self, value: Any)-> Optional[int]: #dovrebbe restituire un intero, ma potrebbe anche dare None
        if value is None:
            return None

        if isinstance(value, str):  # = se il valore che ho è una stringa (fai tutto questo sotto)
            txt = value.strip()  #strip() toglie spazi all'inizio e alla fine
            if txt == "" or txt.lower() in {"n/a", "na", "??"}: # se il testo è vuoto o il testo minuscolo è quei casi
                return None                                     # restituisci None

            #tramite la regex tieni soltanto le cifre ed eventualmete il segno meno
            txt = re.sub(r"[^\d\-]", "", txt)

            if txt == "" or txt == "-":
                return None

            try:
                return int(txt)
            except ValueError:
                return None

        if isinstance(value, (int, np.integer)): # = se il valore che ho è un intero (fai tutto questo sotto)
            return int(value)

        return None # se il mio valore è qualsiasi altra cosa return None


    """
    parse_income converte:
    Se ho per esempio euro30.000 -> 30000.00
    se ho 25k --> 25000.00
    """
    def parse_income(self, value: Any) -> Optional[float]:
        if value is None:
            return None

        if isinstance(value, (int, float, np.integer)):
            income = float(value)
            return income

        if not isinstance(value, str):
            return None

        #ho escluso fino a qui tutti i casi tranne la stringa, ma ora me ne devo occupare

        txt = value.strip().lower()

        if txt in {"", "n/a", "na", "??"}:
            return None

        k_match = re.fullmatch(r"([-+]?\d+)\s*k", txt) #se l'ultima lettera è k (= True)
        if k_match:
            return float(k_match.group(1)) * 1000 #prendi tutta la stringa tranne la k * 1000.0

        #fullmatch controlla che k è finale --> 75k prende il 75 e lo moltiplica per 1000

        # ora togliamo simboli euro, spazi e punti separatori delle migliaia
        txt = txt.replace("€", "").replace(" ", ""). replace(".", "")

        try:
            return float(txt)
        except ValueError:
            return None


    # ULTIMA APARTE: prendi yes, 1, 0 o No e li converti in 1 o 0
    def parse_approved(self, value: Any) -> Optional[int]:
        if value is None:
            return None

        if isinstance(value, (int, float, np.integer)):  #se il valore è già un numero
            if int(value) in (0,1):  #se è già numero 0 o 1
                return int(value)  # lo gestiamo
            return None  #altrimenti non lo gestiamo

        if not isinstance(value, str):
            return None

        txt = value.strip().lower()

        if txt in {"1", "yes", "y", "si", "sì", "t", "true"}:
            return 1

        if txt in {"0", "no", "n", "f", "false"}:
            return 0

        return None

#Validatore --> decidi se metodo è accettabile per il training
class RecordValidator:
    def is_valid(self, rec: CleanRecord) -> bool: #qualsiasi element che inizia con is deve essere booleano

        if rec.age < 18 or rec.age > 99:
            return False

        if rec.income <= 0:
            return False

        if rec.debts < 0 or rec.debts > 50:
            return False

        if rec.credit_score < 300 or rec.credit_score > 850:
            return False

        if rec.approved not in (0,1):
            return False

        return True


# richiamiamo quello che abbiamo fatto, costruire matrici X e Y, poi feature engineering, normalizzare e poi split
# in train e test
class PreprocessingPipeline:
    def __init__(self, parser: FieldParser, validator: RecordValidator):
        self.parser = parser
        self.validator = validator
        self.dropped_records: int = 0
        self.kept_records: int = 0

    def clean_records(self, raw_records: List[Dict[str, Any]]) -> List[CleanRecord]:
        #lista nuova con record puliti e validi
        cleaned: List[CleanRecord] = []

        for row in raw_records:
            age = self.parser.parse_int(row.get("age"))
            income = self.parser.parse_income(row.get("income"))
            debts = self.parser.parse_int(row.get("debts"))
            credit_score = self.parser.parse_int(row.get("credit_score"))
            approved = self.parser.parse_approved(row.get("approved"))

            if None in (age, income, debts, credit_score, approved):
                self.dropped_records += 1
                continue

            rec = CleanRecord(
                age= int(age),
                income= float(income),
                debts= int(debts),
                credit_score= int(credit_score),
                approved= int(approved),
            )

            if not self.validator.is_valid(rec):
                self.dropped_records += 1
                continue

            cleaned.append(rec)
            self.kept_records += 1

        return cleaned

    def build_xy(self, cleaned: List[CleanRecord]) -> Tuple[np.ndarray, np.ndarray]:
        X = np.array(
            [[r.age, r.income, r.debts, r.credit_score] for r in cleaned],
                dtype= float

        )

        y = np.array(
            [r.approved for r in cleaned],
            dtype= int
        )

        return X, y


    def add_feature_engineering(self, X: np.ndarrayy) -> np.ndarray:
        #estraiamo colonna del reddito e poi del debito
        income = X[:, 1]
        debts = X[:, 2]

        debt_to_income = debts / income

        debt_to_income = debt_to_income.reshape(-1, 1) #inverte la forma della matrice

        #aggiungiamo la nuova colonna alla matrice
        X_enhanced = np.hstack((X, debt_to_income))

        return X_enhanced

    #NORMALIZZAZIONE
    def minmax_normalize(self, X: np.ndarray) -> np.ndarray:
        min_col = np.min(X, axis=0)  #0 lavoriamo sulle colonne
        max_col = np.max(X, axis=0)

        # se una colonna è costante, ovvero max=min, il denom = 0
        denom = (max_col - min_col)
        denom[denom == 0] = 1.0  # se denom = 0, ogni colonna è = 1.0

        #applichiamo normalizzazione
        X_norm = (X-min_col) /denom

        return X_norm


    #DIVIDI TRAIN E TEST
    def train_test_split(
            self,
            X: np.ndarray,
            y: np.ndarray,
            train_ratio: float = 0.8,
            seed: int = 42
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:  #2 di training e 2 di tests
        idx = np.arange(len(X))

        rng = np.random.default_rng(seed)
        rng.shuffle(idx)

        train_size = int(len(idx) * train_ratio)

        train_idx = idx[:train_size]
        test_idx = idx[train_size:]

        X_train = X[train_idx]
        X_test = X[test_idx]

        y_train = y[train_idx]
        y_test = y[test_idx]

        return X_train, X_test, y_train, y_test















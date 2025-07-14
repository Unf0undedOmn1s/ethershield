# Phishing Detection using XGBoost

## Τι είναι το XGBoost;

Το XGBoost (Extreme Gradient Boosting) είναι ένας ισχυρός αλγόριθμος μηχανικής μάθησης που βασίζεται σε decision trees και χρησιμοποιεί boosting για να βελτιώνει προοδευτικά τα λάθη του. Είναι ιδανικός για structured/tabular δεδομένα και επιτυγχάνει υψηλή ακρίβεια με χαμηλό υπολογιστικό κόστος.

## Τι πρέπει να μάθεις πρώτα:

- Python (NumPy, pandas)
- Τι είναι supervised learning
- Τι είναι classification
- Πώς λειτουργούν τα Decision Trees
- Τι είναι το Boosting
- Πώς γίνεται train/test split
- Πώς να αξιολογείς μοντέλα (accuracy, precision, recall, F1-score)
- Πώς να χρησιμοποιείς τη βιβλιοθήκη xgboost

## Τι να προσέξεις:

- Πρέπει να κάνεις καλό feature engineering. Το μοντέλο δεν μπορεί να δουλέψει μόνο με raw URLs ή emails.
- Χρειάζεται balanced dataset. Αν έχεις πολύ περισσότερα "safe" URLs από "phishing", θα εκπαιδευτεί στραβά.
- Υπάρχει ρίσκο overfitting αν δεν κάνεις cross-validation ή regularization.
- Κράτησε τα features σου καθαρά, χωρίς να διαρρέουν το label στο input ("data leakage").

## Features για Phishing Detection

Μπορείς να εξάγεις features από URLs ή emails, όπως:

- `url_length`: μήκος του URL
- `has_ip`: περιέχει IP αντί για domain;
- `has_https`: χρησιμοποιεί HTTPS;
- `count_dots`: πόσα “.” υπάρχουν;
- `has_at_symbol`: περιέχει @;
- `has_double_slash`: περιέχει // πέρα από το https://;
- `domain_age`: ηλικία του domain (με χρήση WHOIS)
- `is_shortened`: χρησιμοποιεί shorteners όπως bit.ly;
- `has_suspicious_words`: "login", "secure", "confirm", "account" κλπ
- `dns_record_exists`: υπάρχει το domain στο DNS;
- `alexa_rank`: global popularity (αν υπάρχει πρόσβαση)

Τα παραπάνω μπορούν να εξαχθούν σε Python με libraries όπως `tldextract`, `re`, `whois`, `socket`, `requests`.

## Τι κάνει το XGBoost Model

- Εκπαιδεύεται πάνω σε αυτά τα χαρακτηριστικά
- Μαθαίνει patterns που συχνά οδηγούν σε phishing URLs ή emails
- Προβλέπει πιθανότητα phishing (π.χ. score 0.0–1.0 ή binary 0/1)
- Εξάγει feature importance (ποια χαρακτηριστικά βάρυναν περισσότερο)
- Μπορεί να ενσωματωθεί σε real-time API

## Performance & Scalability

| Χαρακτηριστικό | Πληροφορία |
|----------------|------------|
| Accuracy       | > 96% με σωστό feature set |
| Training Time  | Πολύ γρήγορο, ακόμα και σε laptop |
| Memory Usage   | Χαμηλό, δεν χρειάζεται GPU |
| Scaling Up     | Υποστηρίζει παράλληλη εκπαίδευση με multi-threading |
| Deployment     | Λειτουργεί εύκολα σε FastAPI/Flask APIs |
| Explainability | Υποστηρίζει SHAP για ανάλυση γιατί πήρε μια απόφαση |
| Model Size     | Πολύ μικρό συγκριτικά με Deep Learning |
| Latency        | Μπορεί να δώσει prediction σε < 100ms |

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- ROC AUC
- Confusion Matrix

## Χρήσεις σε API / Real-Time Tools

- Browser extensions: ανιχνεύουν phishing σε κλικ
- Email scanners: check subject/body headers
- Web security gateways
- CLI tools (π.χ. `scan_url.py example.com`)

## Conclusion

Το XGBoost είναι η ιδανική αρχή για phishing detection: είναι γρήγορο, ακριβές, εξηγήσιμο και πολύ φιλικό σε ανάπτυξη APIs και prototypes. Δεν χρειάζεται deep learning για να έχεις καλά αποτελέσματα σε phishing detection — τουλάχιστον όχι στο πρώτο στάδιο.


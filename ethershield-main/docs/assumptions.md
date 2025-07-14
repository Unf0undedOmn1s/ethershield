## Υπόθεση 1: Πρόσβαση σε καλής ποιότητας Phishing Data.
# Κίνδυνος: Τα δεδομένα phishing URLs/emails μπορεί να είναι ελλιπή, ξεπερασμένα ή μη αντιπροσωπευτικά των σύγχρονων επιθέσεων.
# Λύση: 
- Συνδυασμός πολλών δημόσιων πηγών όπως PhishTank, OpenPhish, URLhaus.
- Δημιουργία custom data collection pipeline που αντλεί real-time URLs από threat intelligence feeds.

## Υπόθεση 2: Τα χαρ/ικά που εξάγουμε αρκούν για να διακρίνουμε Phishing από Legitimate.
# Κίνδυνος: Νέα phishing τεχνικές μπορεί να παρακάμπτουν τα κλασικά χαρακτηριστικά (όπως SSL ή URL length).
# Λύση:
- Δυναμική Αναβάθμιση.
- Ενσωμάτωση Metadata (Domain Age, WHOIS, JS Behavior).

## Υπόθεση 3: Το API θα μπορεί να απαντά σε πραγματικό χρόνο.
# Κίνδυνος: Οι υποδομές έχουν καθυστέρηση ή είναι resource heavy.
# Λύση:
- Βελτιστοποίηση μοντέλου.
- Scalable Hosting Cloud (AWS Lambda, FastAPI).

## Υπόθεση 4: Οι χρήστες/εταιρίες θα εμπιστεύονται το μοντέλο.
# Κίνδυνος: Έλλειψη διαφάνειας.
# Λύση: Χρήση εργαλείων explainability.
# Εμφάνιση ερμηνειών στον end user (πχ: Suspicious Domain Age + IP Reputation).

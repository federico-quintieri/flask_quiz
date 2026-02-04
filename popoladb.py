from app import create_app, db
from app.models import Quiz


def inserisciDomande():
    questions = [
        # --- Tema: Sviluppo di intelligenza artificiale in Python ---
        {
            "question": "Quale libreria Python è più usata per il machine learning?",
            "answer_a": "NumPy",
            "answer_b": "Pandas",
            "answer_c": "scikit-learn",
            "answer_d": "Matplotlib",
            "correct": 3,
        },
        {
            "question": "Qual è il ruolo di TensorFlow?",
            "answer_a": "Libreria grafica",
            "answer_b": "Creare reti neurali",
            "answer_c": "Gestire database",
            "answer_d": "Creare interfacce web",
            "correct": 2,
        },
        {
            "question": "Quale tipo di apprendimento permette al modello di scoprire pattern da dati non etichettati?",
            "answer_a": "Supervisionato",
            "answer_b": "Non supervisionato",
            "answer_c": "Rinforzo",
            "answer_d": "Semi-supervisionato",
            "correct": 2,
        },
        {
            "question": "Quale libreria Python è specializzata in deep learning?",
            "answer_a": "Seaborn",
            "answer_b": "PyTorch",
            "answer_c": "Flask",
            "answer_d": "Django",
            "correct": 2,
        },
        {
            "question": "Quale funzione serve per dividere dati in training e test in scikit-learn?",
            "answer_a": "train_test_split",
            "answer_b": "fit_transform",
            "answer_c": "predict",
            "answer_d": "cross_val_score",
            "correct": 1,
        },
        # --- Tema: Visione computerizzata ---
        {
            "question": "Quale libreria è più usata per la computer vision in Python?",
            "answer_a": "OpenCV",
            "answer_b": "BeautifulSoup",
            "answer_c": "Requests",
            "answer_d": "Flask",
            "correct": 1,
        },
        {
            "question": "Quale tecnica permette di rilevare bordi in un'immagine?",
            "answer_a": "Gaussian Blur",
            "answer_b": "Edge Detection",
            "answer_c": "Histogram Equalization",
            "answer_d": "Pooling",
            "correct": 2,
        },
        {
            "question": "Cosa fa la convoluzione in una CNN?",
            "answer_a": "Riduce il dataset",
            "answer_b": "Estrae feature locali",
            "answer_c": "Aumenta la risoluzione",
            "answer_d": "Elimina il rumore",
            "correct": 2,
        },
        {
            "question": "Quale metodo è usato per riconoscere volti?",
            "answer_a": "Face Recognition",
            "answer_b": "Text Mining",
            "answer_c": "Random Forest",
            "answer_d": "Tokenization",
            "correct": 1,
        },
        {
            "question": "Quale trasformazione serve per convertire un'immagine in scala di grigi?",
            "answer_a": "cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)",
            "answer_b": "img.flatten()",
            "answer_c": "np.resize(img)",
            "answer_d": "img.transpose()",
            "correct": 1,
        },
        # --- Tema: NLP (Elaborazione del linguaggio Naturale) ---
        {
            "question": "Quale libreria è molto usata per NLP in Python?",
            "answer_a": "NLTK",
            "answer_b": "Seaborn",
            "answer_c": "Flask",
            "answer_d": "Pandas",
            "correct": 1,
        },
        {
            "question": "Cosa si intende per tokenizzazione?",
            "answer_a": "Dividere testo in unità minime",
            "answer_b": "Creare un database",
            "answer_c": "Addestrare una rete neurale",
            "answer_d": "Analizzare immagini",
            "correct": 1,
        },
        {
            "question": "Quale tecnica serve per ridurre le parole alla loro radice?",
            "answer_a": "Stemming",
            "answer_b": "Lemmatization",
            "answer_c": "Tokenization",
            "answer_d": "Vectorization",
            "correct": 1,
        },
        {
            "question": "Cosa rappresentano i word embeddings?",
            "answer_a": "Rappresentazioni vettoriali delle parole",
            "answer_b": "Grafici a barre",
            "answer_c": "Serie temporali",
            "answer_d": "Bordi dell'immagine",
            "correct": 1,
        },
        {
            "question": "Quale modello è famoso per NLP e completamento del testo?",
            "answer_a": "GPT",
            "answer_b": "ResNet",
            "answer_c": "YOLO",
            "answer_d": "Autoencoder",
            "correct": 1,
        },
        # --- Tema: Applicazione AI in Python ---
        {
            "question": "Quale libreria serve per interfacciare un modello AI in un'app Python?",
            "answer_a": "Flask",
            "answer_b": "Matplotlib",
            "answer_c": "NumPy",
            "answer_d": "Pillow",
            "correct": 1,
        },
        {
            "question": "Quale libreria permette di creare interfacce grafiche per AI apps?",
            "answer_a": "Tkinter",
            "answer_b": "OpenCV",
            "answer_c": "NLTK",
            "answer_d": "scikit-learn",
            "correct": 1,
        },
        {
            "question": "Come puoi salvare un modello addestrato in Python?",
            "answer_a": "pickle",
            "answer_b": "requests",
            "answer_c": "os.makedirs",
            "answer_d": "shutil.copy",
            "correct": 1,
        },
        {
            "question": "Come puoi fare predizioni con un modello addestrato?",
            "answer_a": "model.predict()",
            "answer_b": "model.fit()",
            "answer_c": "model.transform()",
            "answer_d": "model.save()",
            "correct": 1,
        },
        {
            "question": "Quale libreria permette di visualizzare i risultati del modello?",
            "answer_a": "Matplotlib",
            "answer_b": "TensorFlow",
            "answer_c": "PyTorch",
            "answer_d": "NLTK",
            "correct": 1,
        },
    ]
    for q in questions:
        quiz = Quiz(
            question=q["question"],
            answer_a=q["answer_a"],
            answer_b=q["answer_b"],
            answer_c=q["answer_c"],
            answer_d=q["answer_d"],
            correct=q["correct"],
        )
        db.session.add(quiz)

    db.session.commit()
    print("Database popolato con successo!")


if __name__ == "__main__":
    app = create_app()
    with app.app_context():  # <<< contesto necessario
        inserisciDomande()

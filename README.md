## Jeu : Deviner un nombre

### Description
Petit jeu en Python où l'utilisateur doit deviner un nombre choisi aléatoirement.

### Technologies
- Python

### Exécution
```bash
python guess_number.py

---

# 📝 PROJET 2 — Gestionnaire de tâches (To-Do List)

## 🎯 Objectif
Ajouter, afficher et supprimer des tâches.

---

## 🛠 Étapes de réalisation (Python)

### 1️⃣ Créer un fichier
- **Add file → Create new file**
- Nom : `todo_list.py`

---

### 2️⃣ Code simple et clair

```python
tasks = []

while True:
    print("\n1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")

    choice = input("Choix : ")

    if choice == "1":
        task = input("Entrer la tâche : ")
        tasks.append(task)
        print("Tâche ajoutée")

    elif choice == "2":
        for i, task in enumerate(tasks):
            print(i + 1, "-", task)

    elif choice == "3":
        num = int(input("Numéro de la tâche : "))
        tasks.pop(num - 1)
        print("Tâche supprimée")

    elif choice == "4":
        break

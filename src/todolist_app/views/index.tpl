<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Créer une Liste de Tâches</title>
</head>
<body>
    <h1>Créer une Nouvelle Liste de Tâches</h1>
    
    <form action="/todolist" method="post">
        <label for="todolist-name">Nom de la liste :</label>
        <input type="text" id="todolist-name" name="todolist-name" required>
        
        <button type="submit">Créer la Liste</button>
    </form>
</body>
</html>

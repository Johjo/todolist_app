<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Créer une Liste de Tâches</title>
</head>
<body>
    <h1>Créer une Nouvelle Liste de Tâches</h1>
    
    <form action="/create_list" method="post">
        <label for="list-name">Nom de la liste :</label>
        <input type="text" id="list-name" name="list_name" required>
        
        <button type="submit">Créer la Liste</button>
    </form>

    % if defined('lists'):
        <h2>Listes existantes :</h2>
        <ul>
            % for todo_list in lists:
                <li>{{ todo_list }}</li>
            % end
        </ul>
    % end
</body>
</html>

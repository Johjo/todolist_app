<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Détails de la Tâche</title>
</head>
<body>
    <h1>Détails de la Tâche</h1>

    % if task:
        <h2>{{ task.name }}</h2>
        <p>UUID de la tâche : {{ task.key }}</p>
        <form action="/task/{{task.key}}/close" method="post">
            <button type="submit">Terminer</button>
        </form>

        <h3>Créer une sous-tâche</h3>
        <form action="/task/{{task.key}}/subtask" method="post">
            <label for="subtask_title">Titre de la sous-tâche :</label>
            <input type="text" id="subtask_title" name="title" required>
            
            <label for="subtask_description">Description :</label>
            <textarea id="subtask_description" name="description"></textarea>
            
            <button type="submit">Créer sous-tâche</button>
        </form>

    % else:
        <p>Tâche non trouvée.</p>
    % end

    % include('history.tpl', events=events)
</body>
</html>

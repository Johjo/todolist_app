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
        <label for="subtask-description">Description de la tâche :</label>
        <input type="text" id="subtask-description" name="subtask_description" required>

        <button type="submit">Ajouter la tâche</button>
        </form>

    % include('task_list.tpl', tasks=task.subtasks)


    % else:
        <p>Tâche non trouvée.</p>
    % end

    % include('history.tpl', events=events)
</body>
</html>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Liste de Tâches</title>
</head>
<body>
    <h1>Liste de Tâches</h1>
    <p>UUID de la liste : {{ todolist.key }}</p>

    <h2>Ajouter une tâche</h2>
    <form action="/todolist/{{ todolist.key }}/task" method="post">
        <label for="task-description">Description de la tâche :</label>
        <input type="text" id="task-description" name="task_description" required>

        <button type="submit">Ajouter la tâche</button>
    </form>

    % include('task_list.tpl', tasks=todolist.tasks)
    % include('history.tpl', events=events)
</body>
</html>
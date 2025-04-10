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
        <p>UUID de la tâche : {{ task.uuid }}</p>
        <p>
            <a href="/todolist/{{ todolist_uuid }}">Retour à la liste</a>
        </p>
    % else:
        <p>Tâche non trouvée.</p>
    % end
</body>
</html>
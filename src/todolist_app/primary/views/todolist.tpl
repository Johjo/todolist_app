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


    <h2>Tâches</h2>
    % if todolist and todolist.tasks:
    <h3>Ouvertes</h3>
        <ul>
        % for task in todolist.tasks:
            % if task.is_opened:
            <li>
                <a href="/task/{{ task.key }}">
                    {{ task.name }}
                </a>
            </li>
            % end
        % end
        </ul>
    <h3>Fermées</h3>
        <ul>
        % for task in todolist.tasks:
            % if not task.is_opened:
            <li>
                <a href="/task/{{ task.key }}">
                    <s> {{ task.name }}</s>
                </a>
            </li>
            % end
        % end
    </ul>
    % else:
        <p>Aucune tâche dans cette liste.</p>
    % end

    % include('history.tpl', events=events)
</body>
</html>
<h2>Tâches</h2>
% if tasks:
<h3>Ouvertes</h3>
    <ul>
    % for task in tasks:
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
    % for task in tasks:
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

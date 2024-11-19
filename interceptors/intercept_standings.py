# replace existing functions
import django.shortcuts as shortcuts
import django.views.decorators.cache as cache

import courses.lib.standings.standings_data as standings_data

cache.cache_page = lambda x: lambda y: y
shortcuts.get_object_or_404 = lambda *args, **kwargs: standings
standings_data.get_standings_data = lambda *args: (data["users"], data["contests"])

# generate polyfill data
import json
from types import SimpleNamespace

__all__ = ["standings", "data"]

standings = SimpleNamespace()

standings.title = "test-title"
standings.label = "test-label"
standings.contest_type = "AC"
standings.enable_marks = False
standings.js_for_contest_mark = "var newCalculateContestMark = function(\n    total_scores,       // двумерный массив пар балла и времени сдачи задач пользователями\n    user_id,            // номер пользователя\n    contest_info        // информация о контесте\n) {\n    return useOldContestMark(total_scores, user_id)\n};"
standings.js_for_total_mark = "var calculateTotalMark = function(\n\tmarks,              // массив оценок за контесты\n\tcoefficients,        //  массив коэффициентов контесто\n\ttotal_score,        // суммарный балл за все контесты\n\tcontest_score,      // массив баллов за контесты\n\tcontest_max_score,  // массив максимальных набранных баллов за контесты\n\tproblem_score,      // двумерный массив набранных баллов за задачи\n\tproblem_max_score,  // двумерный массив максимальных набранных баллов за задач\n\ttotal_users,        // общее количество участников\n\tproblem_accepted    // двумерный массив количества ОК по задаче\n){\n\treturn defaultTotalMark(marks, coefficients);\n};"
standings.js = ""

data = json.load(open("interceptors/response.json"))
# data['users'] = data['users'][:10]

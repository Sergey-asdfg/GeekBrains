This is Coursework of the course Numpy-Pandas-Matplotlib-Sklearn-Part2-Classification of GeekBrains

The main files are: SVaryukhin_solution.ipynb and 2 files in the folder 'course_project': course_project_train.csv and course_project_test.csv

The main task is to predict 'Credit Default' of the test dataset in the file course_project_test.csv

Train dataset is located in the file course_project_train.csv

The full description of the Course work is in the begining of the file SVaryukhin_solution.ipynb, after that there is full script of the solution

the file SVaryukhin_solution.pkl is a final training model of the Coursework

the file SVaryukhin_solution.csv is result of the prediction (of the final model)

any questions are welcome)

Resume from teacher:
Никита Варганов・Преподаватель
Сергей, добрый день.
Метрики качества на тестовом наборе данных:
F1-score: 0.52447, precision: 0.54642, recall: 0.50421

Комментарии по работе:
1. Хорошо, что вы наипсали несколько своих функций, стоило сопроводить функции документацией / описанием.
2. В функции mono_bin хорошо, что вы обрабатываете исключения, но очень плохо делать просто Exception, старайтесь делать обрабатывать исключения определенных типов: TypeError, ValueError, ...
3. Использовать коэффициент корреляция для оценки силы связи признаков и целевой переменной в задаче бинарной классификации, плохой способ, он работает слабо. Следовало выбрать другой способ анализа.
4. У вас сделан очень классный предварительный анализ признаков, но длля анализа распределениия признаков стоило создать отдельную функцию, поскольку подход у вас одинаковый для всех признаков.
5. При проверке гипотез, стоит сначала строить QQ-график, и если он выглядит адекватно, то проверять гипотезу о нормальности более формально.
6. Для создания новых признаков также имело смысл создать отдельную функцию.
7. При маппинге фичей, ручной способ маппинга не очень классный. Если будет гораздо больше уникальных значений, то это операция затянется. Стоило написать функцию для реализации логики маппинга.
8. При масштабировании признаков, вы используете метод scaler.fit_transform и для обучающей выборки, и для тестовой. Правильнее было использовать этот метод для обучающей выборки, а метод transform для тестовой выборки.
9. Разбиение на train / test в пропорции 0.57 / 0.43, несколько спорное. Стоило больше данных использовать для обучения.
10. Кривые обучения (learning_curve) имеет смысл строить в начале, чтобы понять какую долю обучающей выборки стоит использовать для обучения.
11. Модель получилась хорошей, переобучение небольшое есть, но в целом все хорошо.

Курсовой выполнен у вас качественно, особенно этап предварительной обработки данных, и этап построения WOE-переменных.

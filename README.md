# goit-algo-hw-04

Порівняємо три алгоритми сортування на трьох різних об'ємах даних:

Small - 100 чисел від 0 до 100

Medium - 1000 чисел від 0 до 100

Large - 10000 чисел від 0 до 100

| Algorithm          | Time (ms)                 | Size       |
|--------------------|---------------------------|------------|
| Merge Sort         | 0.0010380000021541491     | Small      |
| Insertion Sort     | 0.001458699996874202      | Small      |
| Timsort            | 4.4200001866556704e-05    | Small      |
| ------------------ | ------------------------- | ---------- |
| Merge Sort         | 0.014202099999238271      | Medium     |
| Insertion Sort     | 0.16812370000116061       | Medium     |
| Timsort            | 0.0005900999967707321     | Medium     |
| ------------------ | ------------------------- | ---------- |
| Merge Sort         | 0.21102550000068732       | Large      |
| Insertion Sort     | 16.448124499998812        | Large      |
| Timsort            | 0.007375300003332086      | Large      |
| ------------------ | ------------------------- | ---------- |

Як ми бачимо із результатів застосування алгоритмів сортування,
на малому розмірі даних (масив із 100 чисел),
сортування злиттям та вставками показали однаковий результат,
а вбудоване сортування timsort виявилось на порядок швидшим.

На середньому обсязі даних (1000 цифр), сортування вставками значно відстало від сортування злиттям,
а сортування teamsort взагалі на три порядки випередило інших.

На великому обсязі даних (10000) ці відмінності навіть зросли.

На цих результатах ми наочно бачимо відмінності у часовій складності алгоритмів:

Insertion sort (сортування вставками, найповільніший) - O(n^2)

Merge sort (сортування злиттям, константне О) - O(n⋅log(n))

Timsort (комбінація перших двох, найшвидший) - від O(n) до O(n⋅log(n))

Отже вбудоване сортування timsort є набагато ефективнішим ніж окремі алгоритми,
тож при розв'язанні задач немає потреби писати свої алгоритми сортування.
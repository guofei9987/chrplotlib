import numpy as np


def tidy_label(data, label):
    label = label or [''] * len(data)
    label = label[:len(data)]
    return ['{:2}'.format(str(i)[:2]) for i in label]


def bar_generate_canvas(y):
    height, length = int(max(y)) + 1, y.shape[0]
    canvas = [[0] * height for _ in range(length)]
    for i, j in enumerate(y):
        j = j * 10
        int_part, frac_part = int(j // 10), int(j % 10)
        k = -1
        for k in range(int_part):
            canvas[i][k] = 10
        canvas[i][k + 1] = frac_part
    return canvas


def bar_change_direction(canvas):
    canvas = [i[::-1] for i in canvas]
    return canvas


def bar_add_segment(canvas):
    canvas_c = list()
    height = len(canvas[0])
    for i in canvas:
        canvas_c.append(i)
        canvas_c.append(i)
        canvas_c.append([0] * height)

    return canvas_c


def bar_rotate(canvas):
    return list(zip(*canvas))


def bar(data, label=None, kind='bar'):
    label = tidy_label(data, label)
    canvas = bar_generate_canvas(data)
    if kind == 'bar':
        mark = ' ▂▃▃▄▅▅▆▇▇█'
        canvas = bar_change_direction(canvas)
        canvas = bar_add_segment(canvas)
        canvas = bar_rotate(canvas)
        res = '\n'.join([''.join([mark[col] for col in row]) for row in canvas])
        res = res + '\n' + ' '.join(label) if label else res
    elif kind == 'barh':
        mark = ['  ', '▎ ', '▍ ', '▌ ', '▋ ', '█ ', '█▎', '█▍', '█▌', '█▌', '█▌']
        res = '\n'.join([''.join([label[idx_row]] + [mark[col] for col in row]) for idx_row, row in enumerate(canvas)])
    else:
        raise Exception('kind should be "bar" or "barh"')
    return res


if __name__ == '__main__':
    data = 10 * np.random.rand(20)
    print(bar(data))
    print(bar(data=data, label=range(20)))
    print(bar(data, kind='bar'))
    print(bar(data=data, label=range(20), kind='barh'))

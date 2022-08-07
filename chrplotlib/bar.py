def tidy_label(data, label):
    label = label or [''] * len(data)
    label = label[:len(data)]
    return ['{:2}'.format(str(i)[:2]) for i in label]


def bar_generate_canvas(y, max_height=None, max_length=None):
    height, length = int(max(y)) + 1, y.shape[0]
    height = max(height, max_height) if max_height else height
    length = max(length, max_length) if max_length else length
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


def bar(data, label=None, kind='bar', max_height=None, max_length=None):
    label = tidy_label(data, label)
    canvas = bar_generate_canvas(data, max_height=max_height, max_length=max_length)
    if kind == 'bar':
        mark = ' ▁▂▃▄▅▅▆▇▇█'
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

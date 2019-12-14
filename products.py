import os


# 读取档案
def read_file(filename):
    elctronic_products = []
    with open(filename, 'r', encoding='utf-8')as f:
        for line in f:
            if '商品,价格' in line:
                continue
            name, price = line.strip().split(',')
            elctronic_products.append([name, price])
    return elctronic_products


def print_file(elctronic_products):
    for p in elctronic_products:
        print(p[0], '的价格是', p[1])


def user_input(elctronic_products):
    # 补充档案
    while True:
        name = input('enter the name of the product:')
        if name == 'q':
            break
        price = input('enter the price of the product:')
        elctronic_products.append([name.strip(), price.strip()])
    print(elctronic_products)
    return elctronic_products


def write_file(filename):
    # 写档案
    with open(filename, 'w', encoding='utf-8')as f:
        f.write('商品,价格\n')
        for p in elctronic_products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename = 'products.csv'
    # 全局变量
    global elctronic_products
    if os.path.isfile(filename):
        print('find it')
        elctronic_products = read_file(filename)
    else:
        print('not find the file')
    print_file(elctronic_products)
    elctronic_products = user_input(elctronic_products)
    write_file(filename)


main()

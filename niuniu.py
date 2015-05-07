# 列举出所有牌型为牛牛的情况
# author:tanteng
import itertools,sys

#初始化数据
cards = list(itertools.combinations([1,2,3,4,5,6,7,8,9,10,11,12,13],5))
print(len(cards))
card_name = {1:'A',2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:'J',12:'Q',13:'K'}
Count = 0

#判断牌型是否为牛牛
def is_niuniu(card=None):
	sums = 0
	card_copy = list(map(check_card,list(card)))
	sums = sum(card_copy)

	if sums%10 == 0:#五张牌相加是10的倍数
		new_card = list(itertools.permutations(card,3))#从五张牌取3张进行排列
		for new_c in new_card:
			new_c = list(new_c)
			new_c = list(map(check_card,new_c))
			summ = sum(new_c)
			if (summ%10 == 0):#如果有任意三张牌是10的倍数
				#print(summ)
				print(list(map(show_card, card)))
				global Count
				Count = Count+1
				break

#显示对应的牌的名称
def show_card(card):
	return card_name[card];

#将11,12,13替换成10
def check_card(card):
	if card>10:
		return 10
	else:
		return card

if __name__ == '__main__':
	for card in cards:
		is_niuniu(card)

	print(Count)
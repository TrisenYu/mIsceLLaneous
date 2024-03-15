#! /usr/bin/python3
# -*- coding: utf-8 -*-
# First-Finished-Date: 2023.10.19.22:23
# SPDX-License-Identifier: GPL-2.0
# Author: kisfg@hotmail.com

from collections import defaultdict
EPS: str = '\x00'
END_SIGN: str = '\x01'

production_cnt: int = 0
terminate_cnt: int = 0

# todo: stupid initiation.
FirstSet, FollowSet = defaultdict(list), defaultdict(list)
Predictable_list, Predict_Table = defaultdict(list), defaultdict(list)
ImageFirstSet, ImageFollowSet = defaultdict(list), defaultdict(list)

# 对非终结项的映射列表
AllRight, First_Export = defaultdict(list), dict()
NonTerminateTerms, TerminateTerms, EmptySign = set(), set(), set()


# ====================================================================== FUNCTIONALITY ZONE ======================================================================


def puts() -> None:
	print()


def union(list_1: list, list_2: list) -> list:
	return list(set(set(list_1) | set(list_2)))


def space_spliter(string: str) -> list:
	return string.split(' ')


def NonTerminate_parser(_grammar: list) -> None:
	global EPS, NonTerminateTerms, AllRight, First_Export, production_cnt

	def init_NonTerminate_parser_1by1(string: str) -> None:
		global NonTerminateTerms, AllRight, production_cnt
		# todo: `->` should be another symbol since the morphism is useful in programming or any abstract system.
		LeftRightExpress = string.split(' -> ')
		LeftRightExpress[1] = EPS if LeftRightExpress[1] == ' ' else LeftRightExpress[1]
		NonTerminateTerms.add(LeftRightExpress[0])
		AllRight[LeftRightExpress[0]].append(LeftRightExpress[1])

		if LeftRightExpress[1] == EPS:
			EmptySign.add(LeftRightExpress[0])
			FirstSet[LeftRightExpress[1]].append(EPS)

		First_Export[production_cnt] = LeftRightExpress[0]
		production_cnt += 1

	for rule in _grammar:
		init_NonTerminate_parser_1by1(rule)


def Terminate_parser() -> None:
	global EPS, TerminateTerms, FirstSet, AllRight, terminate_cnt

	TerminateTerms.add(EPS)
	FirstSet[EPS] = [EPS]

	for rightTerm in AllRight:
		for expression in AllRight[rightTerm]:
			now_term = space_spliter(expression)
			for element in now_term:
				if isNonTerminate(element) or element in TerminateTerms:
					continue
				TerminateTerms.add(element)
				FirstSet[element] = [element]
				terminate_cnt += 1
	TerminateTerms.add(END_SIGN)
	terminate_cnt += 2	# the size of EPS and END_SIGN


def isNonTerminate(tester: str) -> bool:
	return tester in NonTerminateTerms


def FilterEPS(test_list: list) -> list:
	global EPS
	a = [_ for _ in test_list]
	a.remove(EPS)
	return a


def check_image(origin_set, image_set):
	for _ in origin_set:
		tmp1, tmp2 = origin_set[_], image_set[_]
		for _item in tmp1:
			if _item not in tmp2:
				return False
	return True


def reset_image(origin_set, image_set):
	for _ in origin_set:
		image_set[_] = origin_set[_]


def GetFirstSet():
	global FirstSet, ImageFirstSet, AllRight, EPS

	end_flag = False
	while not end_flag:
		reset_image(FirstSet, ImageFirstSet)

		for _ in AllRight:
			for _express in AllRight[_]:
				_now = space_spliter(_express)
				for item in _now:
					if item in EmptySign:
						FirstSet[_] = union(FirstSet[_], FirstSet[item])
						continue
					if not isNonTerminate(item) or item not in EmptySign:
						FirstSet[_] = union(FirstSet[_], FirstSet[item])
						break
		end_flag = check_image(FirstSet, ImageFirstSet)


def GetFollowSet():
	global FollowSet, ImageFollowSet, AllRight, EPS, First_Export

	FollowSet[First_Export[0]] = [END_SIGN]
	end_flag = False
	while not end_flag:
		reset_image(FollowSet, ImageFollowSet)
		# todo: O(n^2) for Follow set calculating...
		#  maybe there is an elegant method for implementation...
		for RightExpress in AllRight:
			for RightElement in AllRight:
				for _express in AllRight[RightElement]:
					_now = space_spliter(_express)	# search the pos of RightExpress in _now
					if RightExpress not in _now:
						continue
					idx = _now.index(RightExpress)
					if idx + 1 < len(_now):			# not the last one
						nxt = _now[idx + 1]
						if not isNonTerminate(nxt):
							FollowSet[RightExpress] = union(FollowSet[RightExpress], [nxt])
							continue
						if nxt not in EmptySign:
							FollowSet[RightExpress] = union(FollowSet[RightExpress], FirstSet[nxt])
							continue
						FollowSet[RightExpress] = union(FollowSet[RightExpress], FilterEPS(FirstSet[nxt]))
						FollowSet[RightExpress] = union(FollowSet[RightExpress], FollowSet[RightElement])
						continue
					FollowSet[RightExpress] = union(FollowSet[RightExpress], FollowSet[RightElement])
		end_flag = check_image(FollowSet, ImageFollowSet)


def PredictList():
	global Predictable_list, AllRight, FirstSet, FollowSet
	cnt = 0
	for _ in AllRight:
		for express in AllRight[_]:
			_now = space_spliter(express)
			for _item in _now:
				if isNonTerminate(_item) and EPS in FirstSet[_item]:
					Predictable_list[str(cnt)] = union(Predictable_list[str(cnt)], FilterEPS(FirstSet[_item]))
					Predictable_list[str(cnt)] = union(Predictable_list[str(cnt)], FollowSet[_])  # 接着取并集
					continue

				if not isNonTerminate(_item):
					# 能推导到 EPS 的，取并集加入推导出当前语句的项的 Follow。
					Predictable_list[str(cnt)] = union(
						Predictable_list[str(cnt)], FollowSet[_] if _item == EPS else [_item]
					)
				else:
					# 不然一次性取完
					Predictable_list[str(cnt)] = union(Predictable_list[str(cnt)], FirstSet[_item])
				break
			cnt += 1


def PredicTable():
	global Predictable_list, First_Export, production_cnt, TerminateTerms, Predict_Table
	tempArray = []

	for _ in TerminateTerms:
		if _ == EPS:  # and _ != END_SIGN
			continue
		tempArray.append(None)

	for Fa in NonTerminateTerms:
		Predict_Table[Fa] = [_ for _ in tempArray]

	for _ in Predictable_list:
		_fa = First_Export[int(_)]
		tmp = []
		for _test in TerminateTerms:
			if _test == EPS:  # or _test == END_SIGN
				continue
			tmp.append('|' + _ + '|' if _test in Predictable_list[_] else None)

		for index, __ in enumerate(tmp):
			if Predict_Table[_fa][index] is not None and __ is not None:
				Predict_Table[_fa][index] += __
			elif Predict_Table[_fa][index] is None:
				Predict_Table[_fa][index] = __


def Productions2Predictable(_Grammar: list):
	NonTerminate_parser(_Grammar)
	Terminate_parser()
	GetFirstSet()
	GetFollowSet()
	PredictList()
	# Note: actually no need to print predict table...
	PredicTable()


def FormatPrintProductions():
	global AllRight, EPS, END_SIGN
	for _ in AllRight:
		_string, leg = '', len(AllRight[_])
		for idx, c in enumerate(AllRight[_]):
			if c == EPS:
				c = 'ε'
			if idx != leg - 1:
				_string += c + ' | '
				continue
			_string += c
		print(f'{_} -> {_string}')


def FormatPrintPredicTable():
	global TerminateTerms, EPS, END_SIGN, Predict_Table, AllRight

	FormatPrintProductions()
	print('-' * 256)
	print(f'{"":^20}', end='')
	for i in TerminateTerms:
		if i == EPS:
			continue
		print(f'{i:^20}' if i != END_SIGN else f'{"$":^20}', end='')
	puts()

	for idx, _ in enumerate(Predict_Table):
		print(f'{_:^20}', end='')
		for index, val in enumerate(Predict_Table[_]):
			if val is None:
				val = ' '
			print(f'{val:^20}', end='')
		puts()
	for i in range(3):
		puts()


def CLEAN_ALL() -> None:
	global TerminateTerms, Predict_Table, Predictable_list, NonTerminateTerms, First_Export, FirstSet, FollowSet, \
		AllRight, EmptySign, ImageFirstSet, ImageFollowSet, production_cnt, terminate_cnt

	FollowSet, FirstSet, Predictable_list = defaultdict(list), defaultdict(list), defaultdict(list)
	ImageFirstSet, ImageFollowSet = defaultdict(list), defaultdict(list)
	Predict_Table, AllRight = defaultdict(list), defaultdict(list)

	TerminateTerms, NonTerminateTerms, EmptySign = set(), set(), set()
	First_Export = dict()
	terminate_cnt, production_cnt = 0, 0


# ====================================================================== TEST DECLARATION ZONE ======================================================================
grammars0 = [
	"S -> a",
	"S -> ( L )",
	"L -> L , S",
	"L -> S"
]

grammars0_1 = [
	"S -> ( L )",
	"S -> a",
	"L -> S L'",
	"L' -> , S L'",
	"L' ->  "
]

grammars1 = [
	"bor -> bor or band",
	"bor -> band",

	"band -> band and bnot",
	"band -> bnot",

	"bnot -> not bnot",
	"bnot -> ( bor )",
	"bnot -> TRUE",
	"bnot -> FALSE",

	"bnot ->  ",
	"band ->  ",
	"bor ->  "
]

grammars1_1 = [
	"bor -> bor or band",
	"bor -> band",
	"band -> band and bnot",
	"band -> bnot",
	"bnot -> not bnot",
	"bnot -> ( bor )",
	"bnot -> TRUE",
	"bnot -> FALSE"
]

grammars1_2 = [
	"bor -> band T",
	"T -> or band",
	"T ->  ",
	"band -> bnot U",
	"U -> and band",
	"U ->  ",
	"bnot -> not bnot",
	"bnot -> ( bor )",
	"bnot -> TRUE",
	"bnot -> FALSE"
]

grammars3 = [
	"E -> T E'",
	"E' -> + T E'",
	"E' ->  ",
	"T -> F T'",
	"T' -> * F T'",
	"T' ->  ",
	"F -> ( E )",
	"F -> id"
]

grammars4_1 = [
	"E -> T E'",
	"E' -> + T E'",
	"E' ->  ",
	"T -> F T'",
	"T' -> * F T'",
	"T' ->  ",
	"F -> ( E )",
	"F -> id",

	"S -> a",
	"S -> ( L )",
	"L -> L , S",
	"L -> S",

	"bor -> bor or band",
	"bor -> band",
	"band -> band and bnot",
	"band -> bnot",
	"bnot -> not bnot",
	"bnot -> ( bor )",
	"bnot -> TRUE",
	"bnot -> FALSE",
	"band ->  ",
	"bor ->  ",
	"bnot ->  "
]

# Normal 4
grammars4_2 = [
	"E -> T E'",
	"E' -> + T E'",
	"E' ->  ",
	"T -> F T'",
	"T' -> * F T'",
	"T' ->  ",
	"F -> ( E )",
	"F -> id",

	"S -> ( L )",
	"S -> a",
	"L -> S L'",
	"L' -> , S L'",
	"L' ->  ",

	"bor -> band X",
	"X -> or band",
	"X ->  ",
	"band -> bnot U",
	"U -> and band",
	"U ->  ",
	"bnot -> not bnot",
	"bnot -> ( bor )",
	"bnot -> TRUE",
	"bnot -> FALSE"
]

# TestCase 5
grammars5 = [
	"Program -> var Variables begin Operators end",
	"Variables -> Variable ; Variables", "Variables ->  ",
	"Variable -> identifier",
	"Operators -> Operator ; Operators", "Operators ->  ",
	"Operator -> read ( Variable )",
	"Operator -> write ( Variable )"
]

grammars6 = [
	"E -> n S",
	"S -> + n S",
	"S ->  "
]


# ====================================================================== END OF TEST DECLARATION ZONE  ======================================================================


def Tester(_Grammar: list) -> None:
	for _ in range(2):
		puts()
	Productions2Predictable(_Grammar)
	# print(FirstSet, FollowSet)
	FormatPrintPredicTable()
	CLEAN_ALL()


# 10 TestCases.
Tester(grammars0)
Tester(grammars0_1)
Tester(grammars1)
Tester(grammars1_1)
Tester(grammars1_2)
Tester(grammars3)
Tester(grammars4_1)
Tester(grammars4_2)
Tester(grammars5)
Tester(grammars6)

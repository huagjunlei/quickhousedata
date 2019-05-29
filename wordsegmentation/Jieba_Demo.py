# encoding=utf-8
import jieba
sentence = '中文分词是文本处理不可或缺的一步！'
seg_list = jieba.cut(sentence, cut_all=True)
print('全模式：','/'.join(seg_list)) #全模式： 中文/分词/是/文本/文本处理/本处/处理/不可/不可或缺/或缺/的/一步//

seg_list = jieba.cut(sentence, cut_all=False)
print('精确模式：','/'.join(seg_list))#精确模式： 中文/分词/是/文本处理/不可或缺/的/一步/！

seg_list = jieba.cut(sentence)
print('默认精确模式：','/'.join(seg_list))#默认精确模式： 中文/分词/是/文本处理/不可或缺/的/一步/！

seg_list = jieba.cut_for_search(sentence)
print('搜索引擎模式：','/'.join(seg_list))#搜索引擎模式： 中文/分词/是/文本/本处/处理/文本处理/不可/或缺/不可或缺/的/一步/！
from textRank import TextRank



# TODO:输入
text = input()
text = text.replace("\\n", "")
T = TextRank(text, pr_config={'alpha': 0.85, 'max_iter': 100})

# TODO:摘要，目前是 原文句子数//5
sum_len = T.get_sent_len() // 5
sum_output, sum_out_ind = T.get_n_sentences(sum_len)
result_list = [i for _, i in sorted(zip(sum_out_ind, sum_output))]
print('摘要:')
for item in result_list:
    print(item[0])

# TODO:关键词，目前是8个
print('关键词:')
word_output = T.get_n_keywords(8)
for item in word_output:
    print(item[0])

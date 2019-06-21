from sklearn.feature_extraction.text import TfidfVectorizer

content_dict = {0:"Rowen Helen Louise Sullivan was born on 23 February 1993 \
in England. Her parents were Diane Sullivan, who was a \
British citizen, and Doreen Margaret Shields, who was born \
in New Zealand. As Diane Sullivan was the birth parent only \
her name was recorded on Rowen Sullivan’s birth certificate: \
The family moved to New Zealand in November 1999 and \
both Rowen and Diane Sullivan became permanent residents \
on family grounds. Diane Sullivan and Doreen Shields were \
unable to marry under the Marriage Act 1955 following the \
Court of Appeal decision in Quilter & Ors v Attorney-General \
[1998] 1 NZLR 523: \
Diane Sullivan became terminally ill and Diane Sullivan and \
Doreen Shields investigated the possibility of adoption by \
Doreen Shields, but because they were unable to marry they \
could not be spouses and therefore were unable to jointly \
adopt pursuant to section 3(3) of the Adoption Act 1955. Any \
alternative adoption order would have required the removal \
of Diane Sullivan’s name from the birth certificate. Accord-\
ingly Doreen Shields applied for and was granted additional \
guardian status of Rowen Sullivan under section 23 of the \
Care of Children Act 2004. Doreen Shields’s guardianship \
expired on Rowen Sullivan’s 18th birthday on 23 February \
2011 pursuant to section 28(1)(a) of the Care of Children Act \
2004: \
Diane Sullivan died on 2 August 2010 when Rowen Sullivan \
was 17 years old: \
Rowen Sullivan became a New Zealand citizen on 30 May \
2011. As at that date Doreen Shields was Rowen Sullivan’s \
only living parent but, given the expiration of the guardian-\
ship, it was thought that there was no legal recognition of their \
relationship: \
Accordingly, Doreen Shields and Rowen Sullivan agreed to \
apply for an adoption order, which was made by the Fam-\
ily Court at Upper Hutt on 15 January 2013 (FAM-2012-078-\
000261) in the name of Doreen Shields. However the order \
required the removal of Diane Sullivan’s name from Rowen \
Sullivan’s birth certificate: \
Because Diane Sullivan died prior to the passing of the Mar-\
riage (Definition of Marriage) Amendment Act 2013, there is \
no means, other than by a Private Bill, by which Diane Sulli-\
van’s name can be added to Rowen Sullivan’s birth certificate \
in order that both parents can be recorded as such under the \
Births, Deaths, Marriages, and Relationships Registration Act \
1995:",
1:"Title	This Act is the Sullivan Birth Registration Act 2014.",
				2:"Commencement	This Act comes into force on the day after the date on which it receives the Royal assent.",
				3:"Interpretation	In this Act, unless the context otherwise requires,— \
Registrar-General has the same meaning as in section 2 of \
the Births, Deaths, Marriages, and Relationships Registration \
Act 1995 \
specified adoption order means the adoption order made in \
favour of Doreen Margaret Shields by the Family Court at \
Upper Hutt on 15 January 2013 (FAM-2012-078-000261) in \
respect of Rowen Helen Louise Sullivan.",
				4:"Registration of adoption order to include birth mother’s \
details		The Registrar-General must add, in accordance with section \
24 of the Births, Deaths, Marriages, and Relationships Regis-\
tration Act 1995, the details of Diane Sullivan as birth mother \
on the registration of the birth of Rowen Helen Louise Sulli-\
van (as well as the details of Doreen Margaret Shields) as if— \
(a) a notice under section 23 of the Births, Deaths, Mar-\
riages, and Relationships Registration Act 1995 had \
been received containing that information; and \
(b) the specified adoption order had been made in favour of \
Diane Sullivan and Doreen Margaret Shields.",
				5:"Parents of Rowen Helen Louise Sullivan	Diane Sullivan and Doreen Margaret Shields are, for all pur-\
poses, the parents of Rowen Helen Louise Sullivan. \
Subsection (1) has effect despite the specified adoption order. \
Subsection (1) does not affect section 4."}

content_list = list(content_dict.values())

vectorizer = TfidfVectorizer(stop_words='english') # 去停用词
X = vectorizer.fit_transform(content_list) # 转化成tfidf矩阵
weight = X.toarray() # 5个section的权重列表
words = vectorizer.get_feature_names() # 词列表

result_dict = {} # 结果字典

for i in range(1, len(content_dict)):

	# 词和权重列表合并为字典
	d = dict(zip(words, weight[i]))

	# 排序选前三
	sort = sorted(d.items(), key=lambda x: x[1], reverse=True)

	top3 = sort[:3]
	top3_word = []
	for tuple in top3:
		top3_word.append(tuple[0])

	# 记录到结果字典
	result_dict[i] = top3_word

print(result_dict)

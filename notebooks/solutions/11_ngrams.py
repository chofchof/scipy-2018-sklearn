text = zen.split("\n")
for n in [2, 3, 4]:
    cv = CountVectorizer(ngram_range=(n, n)).fit(text)
    counts = cv.transform(text)
    most_common = np.argmax(counts.sum(axis=0))
    print(f"most common {n}-gram: {cv.get_feature_names()[most_common]}")


for norm in ["l2", None]:
    tfidf_vect = TfidfVectorizer(norm=norm).fit(text)
    data_tfidf = tfidf_vect.transform(text) 
    most_common = tfidf_vect.get_feature_names()[np.argmax(data_tfidf.max(axis=0).toarray())]
    print(f"highest tf-idf with norm={norm}: {most_common}")
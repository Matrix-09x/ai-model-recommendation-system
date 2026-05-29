import numpy as np 


models = np.array(["GPT-4","Claude","Gemini","Grok","Deepseek","Llama"])

metrices = np.array(["Reasoning","Coding","Creativity","Speed","Memory","Accuracy","Cost efficiency"])
scores = np.array([
    [9.8,9.1,9.2,7.5,9,9.7,5.5],
    [9.7,9.9,8.8,9.6,9.8,9,4.5],
    [9,8.8,8.9,8.7,9,8.6,7],
    [8.2,8,7.8,9,8,7.8,5],
    [8.5,9.5,7.5,8.9,9.1,8.2,9.5],
    [8,7.5,8.3,8.8,7.5,7.8,9.2],


])



means = np.mean(scores,axis=1)

for i,mean in enumerate(means) :
    print(f"The mean of {models[i]} model is {mean}")


max_index = np.argmax(means)
maxx = np.max(means)

print(f"Overall strongest model | {models[max_index]}, Average | {maxx}")

min_index = np.argmin(means)
minn = np.min(means)

print(f"Overall weakest model | {models[min_index]}, Average | {minn}")


for i,score in enumerate(scores) :
    strongest_index = np.argmax(score)
    
    print(f"Model | {models[i]} ,Strongest part | {metrices[strongest_index]}")
    

for i,score in enumerate(scores) :
    weakest_index = np.argmin(score)
    
    print(f"Model | {models[i]} ,Weakest part | {metrices[weakest_index]}")


standard_deviation = np.std(scores,axis=1)

for i,std in enumerate(standard_deviation) :

    if std <= 1 :
        print(f"Model | {models[i]} ,Standard deviation | {std} ,Conclusion | Balanced model")

    
    elif std  > 1 and std <= 2 :
        print(f"Model | {models[i]} ,Standard deviation | {std} ,Conclusion | Moderately Specialized model")

    elif std > 2 :
        print(f"Model | {models[i]} ,Standard deviation | {std} ,Conclusion |  Specialized model")

    
# print(means)

ranking = np.argsort(means)[::-1]
# print(ranking)

ranking_list = []


for i,rank in enumerate(ranking) :
    ranking_list.append(f"{i+1}.{models[rank]}")



clean_name = " ".join(ranking_list)

print(clean_name)


maxx = np.argmax(scores,axis=0)


for i,index in enumerate(maxx) :
    print(f"Top {metrices[i]} model | {models[index]} ")



minn = np.argmin(scores,axis=0)


for i,index in enumerate(minn) :
    print(f"Lowest {metrices[i]} model | {models[index]} ")


def calculate_similarity(model) :
    index = np.where(models == model)[0][0]
    model_score = scores[index]

    dot_product = np.dot(scores,model_score)
    matrix_norm = np.linalg.norm(scores,axis=1)
    model_norm = np.linalg.norm(model_score)

    similarity = (dot_product)/(matrix_norm * model_norm)

    similarity[index] = 0

    for i,score in enumerate(similarity) :
        if i != index :
             print(f"Models | {model},{models[i]}, Similarity | {score:2f}")
    
    return similarity

    
similiarity_models = {}

for model in models :
    similiarity_models[model] = calculate_similarity(model)

# print(similiarity_models)






def most_similar_model(model_list) :
    index = np.where(model_list == 0)[0][0]
    index_max = np.argmax(model_list)
    print(f"the most similar model to {models[index]} is {models[index_max]}")


for i in  models :
    most_similar_model(similiarity_models[i])
  


def least_similar_model(model_list)  :
    index = np.where(model_list == 0)[0][0]
    sort = np.argsort(model_list)
    
    print(f"the least similar model to {models[index]} is {models[sort[1]]}")




for i in  models :
    least_similar_model(similiarity_models[i])





for i,model in enumerate(similiarity_models) :
    similiarity_models[model][i] = 1



similarity_models_grid = np.array(list(similiarity_models.values()))
print(similarity_models_grid)


performance_mean  = np.mean(scores[:,:-1],axis=1)

print(performance_mean)


for i,mean in enumerate(performance_mean) :
    
    if mean >= 8 and   scores[i,6]  >= 7:
        print(f"Model | {models[i]} , Based | Cost efficiency vs Performance , Conclusion | Best value model")


    elif mean >= 8 and   scores[i,6]  < 7 :
        print(f"Model | {models[i]} , Based | Cost efficiency vs Performance , Conclusion | Premium model")
  
  
  
    elif mean < 6 and   scores[i,6]  >= 7:
        print(f"Model | {models[i]} , Based | Cost efficiency vs Performance , Conclusion | Budget model")

    elif (mean >=6 and mean < 8) and scores[i,6] >=6  :
        print(f"Model | {models[i]} , Based | Cost efficiency vs Performance , Conclusion | Balanced model")

    else :
        print(f"Model | {models[i]} , Based | Cost efficiency vs Performance , Conclusion | Poor model")

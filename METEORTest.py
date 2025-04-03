import pymeteor.pymeteor as pymeteor

reference = 'In the beginning, God created the heavens and the earth'
candidate = 'In the beginning, God formed the sky and the land'
# In the beginning, God created the heavens and earth 0.8968181818181818
# In the beginning, God made the heavens and the earth 0.8950617283950616
# At the beginning, God created the heavens and the earth 0.8993827160493827
# At the start, God made the heavens and the earth 0.6724489795918367
# In the beginning, God formed the sky and the land 0.6724489795918367

meteor_score = pymeteor.meteor(reference, candidate)
print(meteor_score)
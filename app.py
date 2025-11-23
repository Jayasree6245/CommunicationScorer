from flask import Flask, request, jsonify
app=Flask(__name__)
RUBRIC = {
    "clarity": 0.3,
    "grammer": 0.2,
    "coherence": 0.3,
    "confidence": 0.2
}
def score_transcript(text):
    words=text.split()
    word_count= len(words)
    scores={
         "clarity": 80,
    "grammer": 70,
    "coherence": 85,
    "confidence": 90
    }
    #overall = sum(scores[c] for c in RUBRIC)/sum(RUBRIC.values())
    overall = sum(scores[c] * RUBRIC[c] for c in RUBRIC)
    return {
        "overall_score": round(overall,2),
        "per_criterion": scores,
        "word_count": word_count

    }
@app.route('/score',methods=['POST'])
def score():
    data=request.json
    text=data.get('transcript')
    if not text:
        return jsonify({"error": "No Transcript provided"}),400
    return jsonify(score_transcript(text))
@app.route('/')
def home():
    return open('index.html').read()
if __name__=='__main__':
      app.run(debug=True)
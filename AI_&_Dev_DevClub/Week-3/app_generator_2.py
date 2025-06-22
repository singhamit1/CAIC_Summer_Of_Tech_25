# bonus_ai_generator.py
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class AITweetGenerator:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.tokenizer.pad_token = self.tokenizer.eos_token
    
    def generate_from_keywords(self, key_dictionary):
         # Simple prompt builder
        company = key_dictionary.get('company', 'A company')
        message = key_dictionary.get('message', 'doing something interesting')
        topic = key_dictionary.get('topic', 'the tech industry')

        # Create a prompt
        prompt = f"{company} is {message}. Here's what it means for {topic}:"

        return self.generate_ai_tweet(prompt, max_length=60)

    def generate_ai_tweet(self, prompt, max_length=60):
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        
        with torch.no_grad():
            outputs = self.model.generate(
                inputs,
                max_length=max_length,
                temperature=0.8,
                do_sample=False,
                repetition_penalty=1.2,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        tweet = generated_text[len(prompt):].strip()
        return prompt +" "+ tweet[:200]  # Twitter limit + prompt limit is "80"
    # @app.route('/generate_and_predict', methods=['POST'])
    # def generate_and_predict():
    
    #     data = request.get_json()
    
    # # Generate tweet
    #     generated_tweet = generator.generate_tweet(...)
    
    # # Calculate features from generated tweet
    #     features = extract_features_from_tweet(generated_tweet)
    
    # # Predict likes using your Week 2 model
    #     predicted_likes = model.predict([features])[0]
    
    #     return jsonify({
    #     'generated_tweet': generated_tweet,
    #     'predicted_likes': int(predicted_likes),
    #     'success': True
    # })
from flask import Flask, request, jsonify
app = Flask(__name__)
ai_generator = AITweetGenerator()

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    if "prompt" in data:
        tweet = ai_generator.generate_ai_tweet(data["prompt"])
    elif any(k in data for k in ["company", "message", "topic"]):
        tweet = ai_generator.generate_from_keywords(data)
    else:
        return jsonify({"error": "Invalid input"}), 400

    return jsonify({"tweet": tweet})
if __name__ == '__main__':
    app.run(debug=True, port=5001)

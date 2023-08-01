from flask import Flask, request, jsonify # flask paketinden gerekli modülleri içe aktarır
app = Flask(__name__) # flask uygulamasını oluşturur

@app.route("/hello", methods=["GET"]) # /hello adresine GET isteği geldiğinde çalışacak fonksiyonu tanımlar
def hello(): # fonksiyonun adı
    name = request.args.get("name", "World") # istekte name adında bir parametre varsa alır, yoksa World değerini kullanır
    return jsonify({"message": f"Hello, {name}!"}) # JSON formatında bir mesaj döndürür

if __name__ == "__main__": # eğer dosya doğrudan çalıştırılıyorsa
    app.run(debug=True) # uygulamayı debug modunda çalıştırır
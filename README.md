# Linebot-Basic
基本LineBot code，其執行後會重複你說的話，是個學舌鳥的功能。<br />
至於如何部屬，請參考[小秘書建置](https://medium.com/pythonstock/%E4%BB%80%E9%BA%BC-%E7%A5%95%E6%9B%B8%E4%B9%9F%E5%BF%AB%E8%A2%AB%E5%8F%96%E4%BB%A3-%E6%89%93%E9%80%A0%E4%BD%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E5%B0%88%E5%B1%AC%E8%A1%8C%E5%8B%95%E7%A5%95%E6%9B%B8-%E9%99%84%E5%AF%A6%E7%8F%BE%E7%A8%8B%E5%BC%8F%E7%A2%BC-f10ef081629 "")

## 檔案解說
#### Procfile <br />
heroku專用檔案，裏頭有指名執行檔案是app，因此假設您將app.py檔案改名，這裡也要跟著更改，否則會出錯。
#### app.py <br />
主程式。將所有監聽、路由器，都放在這裡面，住要編輯程式也都在這裡面。

#### requirements.txt <br />
下載必要套件。在上傳到雲端空間時，要告訴雲端空間，需要是先載入的套件，都要放在這裡面，就算雲端空間已經載入了，還是不能刪掉喔!


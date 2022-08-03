# NotifyBot-RaspberryPi-Discord
大学の課題で作成したラズベリーパイを用いた通知ボットです  

## 授業目標
GPIOによる入出力を含んだオリジナルシステムの開発

## 制作物
RaspberryPiに接続されたスイッチを押下するとDiscordにて通知を行うシステムを作成した  
なお、状況に応じた表示を7セグメントLEDにて行っている  

### 大まかな動作内容
1. main.py  
LED押下の設定やシステム実行の主部分であるループについて記載している  
ループではスイッチ押下によって切り替わる変数flagの値に応じてbot.pyやsegment.pyを呼び出し、処理を実行している  

2. segment.py  
7セグメントLEDに文字を表示する機能について記載しており、main.pyによって随時関数を呼び出すことにより文字を表示している  

3. bot.py  
Discord Botへの接続や通知について記載したプログラムであり、main.pyから呼び出されることにより処理を実行している  

### 改善点
callingからwelcomeへの遷移について、スイッチ押下ではなくDiscord上でメッセージを送信することによる遷移も考えた。  
しかしながら、bot.pyのclient.runによるループ処理を用いたBot操作中に7セグメントLEDを操作するループ処理の実行を行うことができず、  
また、一度client.runをcloseすると再開することができなかったことから、スイッチ押下による遷移を最終実装とした。  
こちらについて、それぞれの処理を完全に別の処理とすることで問題を解消できるかと考えたが、  
その際の実装方法や変数の受け渡し方法が分からなかったため実装を諦めている。  
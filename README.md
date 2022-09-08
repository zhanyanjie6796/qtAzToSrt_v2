# qtAzToSrt

使用説明：可以參考【程式說明：Azure音頻wav轉srt字幕工具.docx】檔案。


程式説明：
	這支程式是使用python寫的轉字幕工具，後端利用微軟文件(docs.microsoft.com)提供的音檔轉換文字建立字幕的開源碼，前端是使用python寫GUI界面程式，將.wav檔連線到Azure做轉換，建立srt字幕。
	
後端：包裝發佈後，剩下【captioning.exe】
後端的微軟程式我在這裏是把他發佈成.exe檔【captioning.exe】直接在主程式下指令叫用。可以在github上下載：https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/scenarios/python/console/captioning/
專案的下的pyAzCaption資料夾下面有兩支程式(同上述網站)：
【captioning.py】：主程式
【helper.py】：被主程式叫用的副程式。

前端：包裝發佈後，剩下【main.exe】
前端qtAzToSrt資料夾，有兩支程式。
【main.py】：主程式。圖形界面上的功能和利用後端連線到Azure做轉換字幕功能。
【Ui_win.py】：圖形界面。vs code 配合qt設計去產生。


程式語言:python

作者：Jack

Final report 410421235:
(a) the way how you prepare the training samples:
	把題目給的圖先讀進來,再換成陣列形式,再經由𝒘(𝑘 + 1) = 𝐰(𝑘) + 𝛼(𝑡(𝑘) − 𝑎(𝑘))𝐱(𝑘) where 𝐰(𝑘) = 	𝑤1(𝑘), 𝑤2(𝑘), 𝑤3(𝑘)]T, 𝐱(𝑘) = [𝐾1(𝑘),𝐾2(𝑘),𝐼(𝑘)]T, 𝑎(𝑘)=𝐰(𝑘)𝑇𝐱(k), 𝑡(𝑘) = 𝐸(𝑘)來不斷	的訓練w.
(b) all parameters, such as MaxlterLimit,a and e, you used for the training algorithm:
	epoch as Epoch
	maxlimit as maxlterlimit
	x = data
	i as k
	x[0] as K1(k)
	x[1] as K2(k)
	x[2] as I(k)
	ak as a(k)
	e as E 
	ek as e(k)
	w as w
	a as a == 0.00001
(c) the derived weight vector w:
	w = [0.22812437 0.64904842 0.10331737]
(d) the print image I’ decrypted from E’
	轉好的圖已經儲存為 finalpicture.jpg 在資料庫中.
(e) the problem I encountered: 
	First I think the big problem is to understand how to open the picture and make it 	into a array as or problem, next use teacher’s algorithm to training the w and put 	w into the equation 𝐼 =(𝐸 − w1𝐾1 − 𝑤2𝐾2)/𝑤3 to find the finalpicture , I think 		the main problem still is to learn how to use python 套件 correct.
(f) what you have learned from this work:
	在這次作業的過程中,我學到了自學能力的重要性,以及在對於virtual code 轉換到實際程式碼上面的一些技巧ㄝ,	當然還有最重要的就是如何用上課所學的東西應用在實際的操作上.
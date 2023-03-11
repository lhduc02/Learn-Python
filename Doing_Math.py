"""
Cô bé Marica bắt đầu học bậc tiểu học trong năm học này. Bài kiểm tra đầu tiên của cô bé là bài kiểm tra toán.
Cô bé chuẩn bị rất kỹ lưỡng cho bài kiểm tra này. Không những vậy, cô bé còn nhờ anh trai của mình giúp đỡ bằng cách cho cô một vài bài tập.
Trong bài tập này, người anh viết ra dãy số theo thứ tự lần lượt có 1 số 1, 2 số 2, 3 số 3, ...
Bây giờ người anh cho Marica hai số nguyên A vàB và hỏi rằng tổng các số trong dãy có chỉ số từ A đến B bằng bao nhiêu?
Ví dụ, nếu A=1 và B=3 thì nó là tổng của ba số đầu tiên kết quả là 1+2+2=5.

Yêu cầu: Giả thiết rằng người anh đưa ra Q cặp số (A,B) khác nhau và Marica phải trả lời hết các câu hỏi này trong thời gian thật nhanh.
Hãy viết chương trình giúp Marica giải quyết bài toán này.

Input
+ Dòng đầu tiên là số tự nhiên Q – số câu hỏi của người anh (1 ≤ Q ≤ 1000).
+ Q dòng tiếp theo, mỗi dòng chứa một cặp số tự nhiên A,B   (1 ≤ A ≤ B ≤ 10^9).

Output
Đưa ra trên Q dòng, dòng thứ i là đáp án của câu hỏi thứ i.

Sample Test:
Input:
      5
      444 594
      3 452
      890 945
      626 732
      419 807
      
Output:
      4856
      9062
      2394
      3942
      13558
"""

import math
def tong(a, b):
    m = math.ceil((-1+math.sqrt(1+8*a))/2)
    n = math.ceil((-1+math.sqrt(1+8*b))/2)
    s = (n-1)*(n)*(2*n-1)/6 - m*(m+1)*(2*m+1)/6 + (m*(m+1)/2-a+1)*m + (b-n*(n-1)/2)*n
    return int(s)
t = int(input())
for i in range(t):
    a, b = [int(i) for i in input().split()]
    print(tong(a, b))

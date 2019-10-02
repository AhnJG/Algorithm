**max_element(), min_element()**

```c++
#include <algorithm>
using namespace std;

*max_element(arr, arr+size)
*max_element(v.begin(), v.end())
```



**sort** (Quick Sort)

```c++
#include <algorithm>
using namespace std;

sort(arr, arr+size);
sort(v.begin(), v.end());
sort(v.begin(), v.end(), compare); // 사용자 정의 함수 사용
sort(v.begin(), v.end(), greater<자료형>()); // 내림차순
sort(v.begin(), v.end()), less<자료형>()); // 오름차순(default)

```


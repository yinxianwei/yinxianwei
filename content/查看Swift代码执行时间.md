Title: 查看Swift代码执行时间
Date: 2017-08-15 15:43:33



```swift
func measure(title: String!, call: () -> Void) {
    let startTime = CACurrentMediaTime()
    call()
    let endTime = CACurrentMediaTime()
    if let title = title {
        print("\(title): ")
    }
    print("Time - \(endTime - startTime)")
 }
```

<!-- more -->


```swift
func doSomeWork() {
  measure("Array") {
  var ar = [String]()
  for i in 0...10000 {
  ar.append("New elem \(i)")
  }
  }
  measure("Image") {
  let url = NSURL(string: "http://lorempixel.com/1920/1920/")
  let image = UIImage(data:NSData(contentsOfURL:url!)!)
  }
}
```

> Array: Time — 0.0845723639995413
> 
> Image: Time — 1.77442857499955


原文：[<https://medium.com/swift-programming/secret-of-swift-performance-a8ee86060843>](<https://medium.com/swift-programming/secret-of-swift-performance-a8ee86060843>)




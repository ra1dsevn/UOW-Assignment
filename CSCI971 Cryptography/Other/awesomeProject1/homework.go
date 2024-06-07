package main
import (
	"crypto/rand"
	"fmt"
	"math"
	"math/big"
	"strconv"
)
func main() {
	var count int64 //统计冲突次数
	var sample = 1000 //试验次数
	var rate float64
	var sampleRange int64
	sampleRange = int64(math.Pow(2,32)) //2^32的范围内取取随机数
	count = match(sampleRange,sample) //计算实验中的重复次数
	fmt.Printf("count = %d\n",count)
	rate = (float64(count)/float64(sample))*100
	fmt.Printf("rate is %.3f\n",rate)
}
func match(Range int64 ,sample int) int64 { //把t和试验次数传进参数
	var count int64 = 0 //计重复次数
	var nums [80000]int
	for i := 0; i < sample; i++ {//重复统计
		nums = Rond(Range)//生成随机数组
		//开始判断是否有相同的数，相同则记一次
		if containsDuplicate(nums) == true{
			count += 1
		}
	}
	return count
}
func Rond(Range int64) [80000]int{//t= 80000
	var arr[80000] int
	for i := 0; i < 80000; i++{
		result, _ := rand.Int(rand.Reader, big.NewInt(Range))
		number := result.String()
		//fmt.Println(number)//打印随机生成的
		num, err := strconv.Atoi(number)
		if err == nil{
			//fmt.Printf(" ")
		}
		arr[i] = num

	}
	return arr
}
func containsDuplicate(num [80000]int) bool {//判断是否冲突，即生日相同的一天
	set := map[int]struct{}{}
	for _ , v := range num {
		if _, has := set[v]; has {
			return true
		}
		set[v] = struct{}{}
	}
	return false
}
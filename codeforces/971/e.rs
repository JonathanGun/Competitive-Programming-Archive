use std::io::{self, BufRead};

fn read_line() -> String {
    let stdin = io::stdin();
    stdin.lock().lines().next().unwrap().unwrap()
}

fn sum_seq(a: i64, b: i64) -> i64 {
    (a + b) * (b - a + 1) / 2
}

fn solve() -> i64 {
    // input a and b integer, from one line, separated by space
    let line = read_line();
    let mut ab = line.split_whitespace();
    let n: i64 = ab.next().unwrap().parse().unwrap();
    let k: i64 = ab.next().unwrap().parse().unwrap();
    let a: i64 = k;
    let b: i64 = a + n - 1;
    // print b-a
    // binary search from a to b
    let mut l = a;
    let mut r = b;
    let mut ans = sum_seq(l, r);
    while l < r {
        let m = (l + r) / 2;
        let left_sum = sum_seq(a, m).abs();
        let right_sum = sum_seq(m + 1, b).abs();
        // abs difference between left and right sum
        let diff = (left_sum - right_sum).abs();
        if diff <= ans {
            ans = diff
        }
        if left_sum < right_sum {
            l = m + 1;
        } else {
            r = m;
        }
    }
    return ans;
}

fn main() {
    // input variable t integer
    let t: i64 = read_line().parse().unwrap();
    // Call solve function t times
    for _ in 0..t {
        println!("{}", solve());
    }
}

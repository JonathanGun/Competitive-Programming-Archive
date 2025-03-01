use std::io::{self, BufRead};
use std::cmp::max;

fn read_line() -> String {
    let stdin = io::stdin();
    stdin.lock().lines().next().unwrap().unwrap()
}

fn solve() {
    // input x, y, k integer
    let line = read_line();
    let mut xyk = line.split_whitespace();
    let x: i32 = xyk.next().unwrap().parse().unwrap();
    let y: i32 = xyk.next().unwrap().parse().unwrap();
    let k: i32 = xyk.next().unwrap().parse().unwrap();

    // Perform ceiling division using modulo
    let x_div_k = (x + k - 1) / k;
    let y_div_k = (y + k - 1) / k;

    let mut ans: i32 = max(x_div_k, y_div_k) * 2;
    if y < x && y_div_k < x_div_k {
        ans -= 1;
    }
    println!("{}", ans);
}

fn main() {
    // input variable t integer
    let t: i32 = read_line().parse().unwrap();
    // Call solve function t times
    for _ in 0..t {
        solve();
    }
}

use std::io::{self, BufRead};

fn read_line() -> String {
    let stdin = io::stdin();
    stdin.lock().lines().next().unwrap().unwrap()
}

fn solve() {
    // input a and b integer, from one line, separated by space
    let line = read_line();
    let mut ab = line.split_whitespace();
    let a: i32 = ab.next().unwrap().parse().unwrap();
    let b: i32 = ab.next().unwrap().parse().unwrap();
    // print b-a
    println!("{}", b - a);
}

fn main() {
    // input variable t integer
    let t: i32 = read_line().parse().unwrap();
    // Call solve function t times
    for _ in 0..t {
        solve();
    }
}

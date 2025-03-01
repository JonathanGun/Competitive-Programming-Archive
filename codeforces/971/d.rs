use std::io::{self, BufRead};

fn read_line() -> String {
    let stdin = io::stdin();
    stdin.lock().lines().next().unwrap().unwrap()
}

fn solve() {
    let n: i32 = read_line().parse().unwrap();
    // vector 1D array of integer size n
    let mut y0 = Vec::with_capacity(n as usize);
    let mut y1 = Vec::with_capacity(n as usize);
    for _ in 0..n {
        // input a and b integer, from one line, separated by space
        let line = read_line();
        let mut ab = line.split_whitespace();
        let x: i32 = ab.next().unwrap().parse().unwrap();
        let y: i32 = ab.next().unwrap().parse().unwrap();
        if y == 0 {
            y0.push(x);
        } else {
            y1.push(x);
        }
    }

    // sort y0 and y1
    y0.sort();
    y1.sort();

    // base case: where x equal, 1st point from y0, 2nd point from y1, add other points as the third point (there are n - 2 points)
    // two pointer over y0 and y1, add to ans if y0[i] == y1[j]
    let mut i: usize = 0;
    let mut j: usize = 0;
    let mut ans: i64 = 0;
    while i < y0.len() && j < y1.len() {
        if y0[i] == y1[j] {
            ans += n as i64 - 2;
        }
        if y0[i] < y1[j] {
            i += 1;
        } else {
            j += 1;
        }
    }

    // edge case:: where x not equal, 1st point from y0, 2nd point from y1, check if there are 3rd eligible point
    // eligible point is: if 1st point < 2nd point, 3rd point is 1st point + 1, otherwise (2nd point < 1st point), 3rd point is 2nd point - 1
    // iterate through y0, check if y0[i] + 1 is in y1, and y0[i] + 2 is in y0
    for i in 0..y0.len() {
        if y1.binary_search(&(y0[i] + 1)).is_ok() && y0.binary_search(&(y0[i] + 2)).is_ok() {
            ans += 1;
        }
    }
    for i in 0..y1.len() {
        if y0.binary_search(&(y1[i] - 1)).is_ok() && y1.binary_search(&(y1[i] - 2)).is_ok() {
            ans += 1;
        }
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

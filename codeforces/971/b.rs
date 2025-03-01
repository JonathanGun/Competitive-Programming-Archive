use std::io::{self, BufRead};

fn read_line() -> String {
    let stdin = io::stdin();
    stdin.lock().lines().next().unwrap().unwrap()
}

fn solve() {
    let n: i32 = read_line().parse().unwrap();
    // input 2D array of char size Nx4, use static array with_capacity
    let mut a = Vec::with_capacity(n as usize);
    for _ in 0..n {
        let line = read_line();
        let mut row: Vec<char> = Vec::with_capacity(4);
        for c in line.chars() {
            row.push(c);
        }
        a.push(row);
    }
    // iterate the array but in reversed order
    for i in (0..n).rev() {
        for j in 0..4 {
            if a[i as usize][j as usize] == '#' {
                // print j+1 without enter
                print!("{} ", j + 1);
                // break
                break;
            }
        }
    }
    println!();
}

fn main() {
    // input variable t integer
    let t: i32 = read_line().parse().unwrap();
    // Call solve function t times
    for _ in 0..t {
        solve();
    }
}
use std::{io, vec};
use std::io::prelude::*;

fn read<T>(si: &mut T) -> String where T: Read {
    let mut s = String::new();
    si.read_to_string(&mut s).unwrap();
    s
}

fn next<T>(it: &mut std::str::SplitAsciiWhitespace) -> T where
    T: std::str::FromStr,
    <T as std::str::FromStr>::Err: std::fmt::Debug {
    it.next().unwrap().parse().unwrap()
}

fn to_base_7(n: i32, d: i32, f: usize, l: usize) -> String {

    let mut base_7 = String::new();
    let mut fraction = n % d;
    
    for _ in 0..=l {
        fraction *= 7;
        base_7.push_str(&(fraction / d).to_string());
        fraction %= d;
    }

    base_7[f..=l].to_string()
}
fn main() {
    // 입력
    let mut si = io::BufReader::new(io::stdin().lock());
    let mut so = io::BufWriter::new(io::stdout().lock());
    let s = read(&mut si);
    let mut it = s.split_ascii_whitespace();

    let n = next::<i32>(&mut it);
    for i in 1..=n {
        let a = next::<i32>(&mut it);
        let b = next::<i32>(&mut it);
        let c = next::<usize>(&mut it);
        let d = next::<usize>(&mut it);
        writeln!(so, "Problem set {}: {} / {}, base 7 digits {} through {}: {}",i,a,b,c,d,to_base_7(a, b, c, d)).ok();
    }
}
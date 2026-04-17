box = document.querySelector('.box');

box.addEventListener('mouseover', function(){
    // console.log('Mouse is over the document!');
    gsap.to('.box',{
        trigger: '.box',
        rotation: 180,
        duration: 3,
        yoyo: true,
        ease: 'bounce',
    })
});


// split elements with the class "split" into words and characters
let split = SplitText.create(".split", { type: "words, chars" });

// now animate the characters in a staggered fashion
gsap.from(split.chars, {
  duration: 1, 
  y: 100,       // animate from 100px below
  autoAlpha: 0, // fade in from opacity: 0 and visibility: hidden
  stagger: 0.02,
  ease: "elastic.out(1,0.3)"
});


(define (problem sand-sort-problem) 
    (:domain sand-sort)
    (:objects 
        bottle1 bottle2 bottle3 bottle4 bottle5
        R1 R2 R3
        G1 G2 G3
        B1 B2 B3
    )

    (:init
        (is-on B2 R3) 
        (is-on R3 G1)
        (is-on G2 B3)
        (is-on B3 R2)
        (is-on B1 G3)
        (is-on G3 R1)

        (is-compatible R1 R2) (is-compatible R2 R1)
        (is-compatible R1 R3) (is-compatible R3 R1)
        (is-compatible R2 R3) (is-compatible R3 R2)

        (is-compatible G1 G2) (is-compatible G2 G1)
        (is-compatible G1 G3) (is-compatible G3 G1)
        (is-compatible G2 G3) (is-compatible G3 G2)

        (is-compatible B1 B2) (is-compatible B2 B1)
        (is-compatible B1 B3) (is-compatible B3 B1)
        (is-compatible B2 B3) (is-compatible B3 B2)

        (on-top bottle1 G1)
        (on-top bottle2 R2)
        (on-top bottle3 R1)

        (size-3 bottle1)
        (size-3 bottle2)
        (size-3 bottle3)
        (size-0 bottle4)
        (size-0 bottle5)

    )

    (:goal 
        (and
        
            (is-on R1 R2)
            (is-on R2 R3)
            (is-on B1 B2)
            (is-on B2 B3)
            (is-on G1 G2)
            (is-on G2 G3)

        )
    
            

    )


    )

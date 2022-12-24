(define (domain sand-sort)
  (:requirements :negative-preconditions :disjunctive-preconditions)
  (:predicates
   (is-on ?c1 ?c2) ;c2 este deasupra lui c1
   (is-compatible ?c1 ?c2)
   (on-top ?s ?c) 
   (size-0 ?s)
   (size-1 ?s)
   (size-2 ?s)
   (size-3 ?s)
  )

  ;from size 3 to size 2
  (:action pour-3-to-2
    :parameters (?s1 ?s2 ?c1 ?c2 ?c3) ;c1 este pe c3 in sticla s1
    :precondition (and (size-3 ?s1)
                       (size-2 ?s2)
                       (is-compatible ?c1 ?c2)
                       (on-top ?s1 ?c1)
                       (on-top ?s2 ?c2)
                       (is-on ?c3 ?c1) 
                       )
    :effect (and (size-2 ?s1)
                 (size-3 ?s2)
                 (not(size-3 ?s1))
                 (not(size-2 ?s2))
                 (on-top ?s2 ?c1)
                 (on-top ?s1 ?c3)
                 (not (on-top ?s1 ?c1))
                 (not (on-top ?s2 ?c2))
                 (is-on ?c2 ?c1)
                 (not(is-on ?c3 ?c1))
                 ))


  ;from size 3 to size 1
  (:action pour-3-to-1
    :parameters (?s1 ?s2 ?c1 ?c2 ?c3) ;c1 este pe c3 in sticla s1
    :precondition (and (size-3 ?s1)
                       (size-1 ?s2)
                       (is-compatible ?c1 ?c2)
                       (on-top ?s1 ?c1)
                       (on-top ?s2 ?c2)
                       (is-on ?c3 ?c1) 
                       )
    :effect (and (size-2 ?s1)
                 (size-2 ?s2)
                 (not(size-3 ?s1))
                 (not(size-1 ?s2))
                 (on-top ?s2 ?c1)
                 (on-top ?s1 ?c3)
                 (not (on-top ?s1 ?c1))
                 (not (on-top ?s2 ?c2))
                 (is-on ?c2 ?c1)
                 (not(is-on ?c3 ?c1))
                 ))



  ;from size 3 to size 0
  (:action pour-3-to-0
    :parameters (?s1 ?s2 ?c1 ?c3) ;c1 este pe c3 in sticla s1
    :precondition (and (size-3 ?s1)
                       (size-0 ?s2)
                       (on-top ?s1 ?c1)
                       (is-on ?c3 ?c1) 
                       )
    :effect (and (size-2 ?s1)
                 (size-1 ?s2)
                 (not(size-3 ?s1))
                 (not(size-0 ?s2))
                 (on-top ?s2 ?c1)
                 (on-top ?s1 ?c3)
                 (not (on-top ?s1 ?c1))
                 (not(is-on ?c3 ?c1))
                 ))                            
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


    ;from size 2 to size 2
  (:action pour-2-to-2
    :parameters (?s1 ?s2 ?c1 ?c2 ?c3) ;c1 este pe c3 in sticla s1
    :precondition (and (size-2 ?s1)
                       (size-2 ?s2)
                       (is-compatible ?c1 ?c2)
                       (on-top ?s1 ?c1)
                       (on-top ?s2 ?c2)
                       (is-on ?c3 ?c1) 
                       )
    :effect (and (size-1 ?s1)
                 (size-3 ?s2)
                 (not(size-2 ?s1))
                 (not(size-2 ?s2))
                 (on-top ?s2 ?c1)
                 (on-top ?s1 ?c3)
                 (not (on-top ?s1 ?c1))
                 (not (on-top ?s2 ?c2))
                 (is-on ?c2 ?c1)
                 (not(is-on ?c3 ?c1))
                 ))


  ;from size 2 to size 1
  (:action pour-2-to-1
    :parameters (?s1 ?s2 ?c1 ?c2 ?c3) ;c1 este pe c3 in sticla s1
    :precondition (and (size-2 ?s1)
                       (size-1 ?s2)
                       (is-compatible ?c1 ?c2)
                       (on-top ?s1 ?c1)
                       (on-top ?s2 ?c2)
                       (is-on ?c3 ?c1) 
                       )
    :effect (and (size-1 ?s1)
                 (size-2 ?s2)
                 (not(size-2 ?s1))
                 (not(size-1 ?s2))
                 (on-top ?s2 ?c1)
                 (on-top ?s1 ?c3)
                 (not (on-top ?s1 ?c1))
                 (not (on-top ?s2 ?c2))
                 (is-on ?c2 ?c1)
                 (not(is-on ?c3 ?c1))
                 ))



  ;from size 2 to size 0
  (:action pour-2-to-0
    :parameters (?s1 ?s2 ?c1 ?c3) ;c1 este pe c3 in sticla s1
    :precondition (and (size-2 ?s1)
                       (size-0 ?s2)
                       (on-top ?s1 ?c1)
                       (is-on ?c3 ?c1) 
                       )
    :effect (and (size-1 ?s1)
                 (size-1 ?s2)
                 (not(size-2 ?s1))
                 (not(size-0 ?s2))
                 (on-top ?s2 ?c1)
                 (on-top ?s1 ?c3)
                 (not (on-top ?s1 ?c1))
                 (not(is-on ?c3 ?c1))
                 ))           

    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;   


     ;from size 1 to size 2
  (:action pour-1-to-2
    :parameters (?s1 ?s2 ?c1 ?c2)
    :precondition (and (size-1 ?s1)
                       (size-2 ?s2)
                       (is-compatible ?c1 ?c2)
                       (on-top ?s1 ?c1)
                       (on-top ?s2 ?c2)
                       )
    :effect (and (size-0 ?s1)
                 (size-3 ?s2)
                 (not(size-1 ?s1))
                 (not(size-2 ?s2))
                 (on-top ?s2 ?c1)
                 (not (on-top ?s1 ?c1))
                 (not (on-top ?s2 ?c2))
                 (is-on ?c2 ?c1)
                 ))


  ;from size 1 to size 1
  (:action pour-1-to-1
    :parameters (?s1 ?s2 ?c1 ?c2) 
    :precondition (and (size-1 ?s1)
                       (size-1 ?s2)
                       (is-compatible ?c1 ?c2)
                       (on-top ?s1 ?c1)
                       (on-top ?s2 ?c2)
                       )
    :effect (and (size-0 ?s1)
                 (size-2 ?s2)
                 (not(size-1 ?s1))
                 (not(size-1 ?s2))
                 (on-top ?s2 ?c1)
                 (not (on-top ?s1 ?c1))
                 (not (on-top ?s2 ?c2))
                 (is-on ?c2 ?c1)
                 ))



  ;from size 1 to size 0
  (:action pour-1-to-0
    :parameters (?s1 ?s2 ?c1)
    :precondition (and (size-1 ?s1)
                       (size-0 ?s2)
                       (on-top ?s1 ?c1)
                       )
    :effect (and (size-0 ?s1)
                 (size-1 ?s2)
                 (not(size-1 ?s1))
                 (not(size-0 ?s2))
                 (on-top ?s2 ?c1)
                 (not (on-top ?s1 ?c1))

                 ))                                                  

)
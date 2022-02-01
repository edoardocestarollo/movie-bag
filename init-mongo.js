db.createUser(
    {
        user: "flask",
        pwd: "ciao",
        roles: [ {
            role: "dbOwner",
            db: "moviedb"
        }, "dbOwner" ],
        mechanisms: [ "SCRAM-SHA-1"],

    }
)
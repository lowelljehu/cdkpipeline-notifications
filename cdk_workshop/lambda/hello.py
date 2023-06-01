import json

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': """ <!DOCTYPE html>
                    <html lang="en">
                    <!--
                        The first iteration and a static version of the Mythical Mysfits website.
                        This site does not integrate with any service backend for dynamic content.
                        All of the mysfits displayed are provided as JSON objects directly within
                        the JavaScript at the end of this file.
                    -->
                    <head>
                        <title>Mythical Mysfits</title>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.6/angular.min.js"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
                        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css">
                    </head>
                    <body ng-app="mysfitsApp" style="background-color:#FFCCCB">
                        <style>
                        @media (max-width: 800px) {
                            img {
                            max-width: 300px;
                            }
                        }
                        </style>
                        <br>
                        <div style="text-align: center">
                        <img src="https://www.mythicalmysfits.com/images/mysfits_banner.gif" width="800px" align="center">
                        </div>
                        <div class="container">
                        <div id="mysfitsGrid" class="row" ng-controller="mysfitsListController">
                            <div class="col-md-4 border border-warning" ng-repeat="mysfit in mysfits">
                                <br>
                                <p align="center">
                                    <strong> {{mysfit.name}}</strong>
                                    <br>
                                    <img src="{{mysfit.thumbImageUri}}" alt="{{mysfit.Name}}">
                                </p>
                                <p>
                                    <br>
                                    <b>Species:</b> {{mysfit.species}}
                                    <br>
                                    <b>Age:</b> {{mysfit.age}}
                                    <br>
                                    <b>Good/Evil:</b> {{mysfit.goodevil}}
                                    <br>
                                    <b>Lawful/Chaotic:</b> {{mysfit.lawchaos}}
                                </p>
                            </div>
                            </div>
                        </div>
                        <p>
                        <br>
                        <br>
                        &nbsp;&nbsp;This site was created for use in the AWS Modern Application Workshop. <a href="https://github.com/aws-samples/aws-modern-application-workshop">Please see details here.</a>
                        </p>
                    </body>
                    <script>

                        var app = angular.module('mysfitsApp', []);

                        var gridScope;

                        app.controller('mysfitsListController', function($scope) {

                        // the list of Mysfits to be displayed on the MythicalMysfits website.
                        $scope.mysfits =
                            [
                            {
                                "mysfitId": "4e53920c-505a-4a90-a694-b9300791f0ae",
                                "name": "Evangeline",
                                "species": "Chimera",
                                "age": 43,
                                "goodevil": "Evil",
                                "lawchaos": "Lawful",
                                "thumbImageUri": "https://www.mythicalmysfits.com/images/chimera_thumb.png"
                            },
                            {
                                "mysfitId": "2b473002-36f8-4b87-954e-9a377e0ccbec",
                                "name": "Pauly",
                                "species": "Cyclops",
                                "age": 2,
                                "goodevil": "Neutral",
                                "lawchaos": "Lawful",
                                "thumbImageUri": "https://www.mythicalmysfits.com/images/cyclops_thumb.png"
                            },
                            {
                                "mysfitId": "0e37d916-f960-4772-a25a-01b762b5c1bd",
                                "name": "CoCo",
                                "species": "Dragon",
                                "age": 501,
                                "goodevil": "Good",
                                "lawchaos": "Chaotic",
                                "thumbImageUri": "https://www.mythicalmysfits.com/images/dragon_thumb.png"
                            },
                            {
                                "mysfitId": "da5303ae-5aba-495c-b5d6-eb5c4a66b941",
                                "name": "Gretta",
                                "species": "Gorgon",
                                "age": 31,
                                "goodevil": "Evil",
                                "lawchaos": "Neutral",
                                "thumbImageUri": "https://www.mythicalmysfits.com/images/gorgon_thumb.png"
                            },
                            {
                                "mysfitId": "b41ff031-141e-4a8d-bb56-158a22bea0b3",
                                "name": "Snowflake",
                                "species": "Yeti",
                                "age": 13,
                                "goodevil": "Evil",
                                "lawchaos": "Neutral",
                                "thumbImageUri": "https://www.mythicalmysfits.com/images/yeti_thumb.png"
                            },
                            {
                                "mysfitId": "3f0f196c-4a7b-43af-9e29-6522a715342d",
                                "name": "Gary",
                                "species": "Kraken",
                                "age": 2709,
                                "goodevil": "Neutral",
                                "lawchaos": "Chaotic",
                                "thumbImageUri": "https://www.mythicalmysfits.com/images/kraken_thumb.png"
                            }
                            ]
                        });


                    </script>
                    </html> """
                        }


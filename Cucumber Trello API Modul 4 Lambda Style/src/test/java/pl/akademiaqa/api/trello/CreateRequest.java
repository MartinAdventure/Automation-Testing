package pl.akademiaqa.api.trello;

import io.restassured.response.Response;
import lombok.RequiredArgsConstructor;
import pl.akademiaqa.handlers.api.RequestHandler;


import static io.restassured.RestAssured.given;

@RequiredArgsConstructor
public class CreateRequest {

    private final BaseRequest baseRequest;

    public Response create(RequestHandler requestHandler) {

        return given()
                .spec(baseRequest.requestSetup(requestHandler.getQueryParams()))
                .when()
                .post(requestHandler.getEndpoint())
                .then()
                .log().ifError()
                .extract()
                .response();
    }
}

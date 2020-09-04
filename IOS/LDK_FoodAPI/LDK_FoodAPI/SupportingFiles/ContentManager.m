//
//  ContentManager.m
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "ContentManager.h"

@implementation ContentManager

+ (ContentManager *)sharedManager {
    static ContentManager *manager = nil;
    static dispatch_once_t onceToken;
    
    dispatch_once(&onceToken, ^{
        manager = [[ContentManager alloc]init];
    });
    
    return manager;
}

- (void)getFoodListWithCompletion:(void (^)(BOOL, NSArray *, NSString *))callback {
    [self sendBaseRequestWithUrl:API_POSTS header:nil body:nil httpMethod:HTTP_GET completion:^(BOOL success, NSDictionary *getDict, NSString *errorMessage) {
        if (success) {
            NSMutableArray *recipes = [[NSMutableArray alloc] init];
            
            for (NSDictionary *dict in [getDict objectForKey:KEY_RECIPES]) {
                [recipes addObject:[Recipe recipeFromDictionary:dict]];
            }
            
            callback(YES, recipes, nil);
        } else {
            callback(NO, nil, errorMessage);
        }
    }];
}

# pragma mark - API base functions

-(void) sendBaseRequestWithUrl:(NSString *)url header:(NSDictionary *)header body:(NSDictionary *)body httpMethod:(NSString *)method completion:(void(^)(BOOL success, NSDictionary *dict, NSString *errorString))callback{
    Reachability *networkChecking  = [Reachability reachabilityForInternetConnection];
    NetworkStatus status = [networkChecking currentReachabilityStatus];
    
    if (status == NotReachable) {
        callback(NO, nil ,@"There is no internet !");
    } else {
        [self setNetworkLoaderVisible:YES];
        
        //Get global Session
        NSURLSessionConfiguration *configuration = [NSURLSessionConfiguration defaultSessionConfiguration];
        
        //Create new manager with created global configuration & input url String
        manager = [[AFHTTPSessionManager alloc] initWithBaseURL:[NSURL URLWithString:url] sessionConfiguration:configuration];
        
        //Set time out
        [manager.requestSerializer setTimeoutInterval:30.0];
        
        //Set reading json type of Response
        manager.responseSerializer = [AFJSONResponseSerializer serializer];
        
        if ([method isEqualToString:HTTP_GET]) {
            [manager GET:url parameters:body headers:header progress:^(NSProgress * _Nonnull downloadProgress) {
                NSLog(@"download progress, ");
            } success:^(NSURLSessionDataTask * _Nonnull task, id  _Nullable responseObject) {
                callback(YES, responseObject, nil);
            } failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error) {
                NSLog(@"Fail, %@", error);
            }];
        } else if ([method isEqualToString:HTTP_POST]){
            [manager POST:url parameters:body headers:header progress:^(NSProgress * _Nonnull uploadProgress) {
                NSLog(@"");
            } success:^(NSURLSessionDataTask * _Nonnull task, id  _Nullable responseObject) {
                callback(YES, responseObject, nil);
            } failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error) {
                callback(NO, nil, error.localizedDescription);
            }];
        }
    }
}

//- (void)sendBaseRequestWithUrl:(NSString *)url header:(NSDictionary *)header body:(NSDictionary *)body httpMethod:(NSString *)method completion:(void(^)(BOOL success, NSDictionary *getDict, NSString *errorMessage))callback {
//
//    Reachability *networkChecking = [Reachability reachabilityForInternetConnection];
//    NetworkStatus networkStatus = [networkChecking currentReachabilityStatus];
//
//    if (networkStatus == NotReachable) {
//        callback(NO, nil, @"There is no network connection.");
//    } else {
//        [self setNetworkLoaderVisible:YES];
//
//        // Get global session
//        NSURLSession *session = [NSURLSession sharedSession];
//
//        // Create request with input url, header, param and httpMethod
//        NSURLRequest *request = [self createRequestWithUrlString:url header:header body:body httpMethod:method];
//
//        // Create a new data task with created request
//        NSURLSessionDataTask *task = [session dataTaskWithRequest:request completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) {
//
//            NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)response;
//            BOOL success = NO;
//            NSDictionary *dict;
//            NSString *errorMessage;
//
//            if (httpResponse.statusCode == 200) {
//                NSError *error = nil;
//                // Convert data to dictionary
//                dict = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingMutableContainers error:&error];
//
//                if (error) {
//                    errorMessage = @"Error parsing data";
//                } else {
//                    success = YES;
//                }
//            } else {
//                errorMessage = [NSString stringWithFormat:@"Error sending data to server: %ld", (long)httpResponse.statusCode];
//            }
//
//            dispatch_async(dispatch_get_main_queue(), ^{
//                callback(success, dict, errorMessage);
//                [self setNetworkLoaderVisible:NO];
//            });
//        }];
//
//        [task resume];
//    }
//}

- (NSURLRequest *)createRequestWithUrlString:(NSString *)urlString header:(NSDictionary *)header body:(NSDictionary *)body httpMethod:(NSString *)method {
    
    NSURL *url = [NSURL URLWithString:urlString];
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] initWithURL:url];
    
    [request setCachePolicy:NSURLRequestReloadIgnoringCacheData];
    [request setTimeoutInterval:30];
    [request setHTTPMethod:method];
    
    //    [request setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];
    //    [request setValue:@"application/json" forHTTPHeaderField:@"Accept"];
    
    if (header) {
        for (NSString *key in header.allKeys) {
            [request setValue:[header objectForKey:key] forHTTPHeaderField:key];
        }
    }
    
    if (body) {
        NSMutableData *data = [[NSMutableData alloc] init];
        
        for (int i=0; i<body.allKeys.count; i++) {
            NSString *key = [body.allKeys objectAtIndex:i];
            id param = [body objectForKey:key];
            [data appendData:[[NSString stringWithFormat:@"%@=", key] dataUsingEncoding:NSUTF8StringEncoding]];
            [data appendData:[[NSString stringWithFormat:@"%@&", param] dataUsingEncoding:NSUTF8StringEncoding]];
        }
        
        [request setHTTPBody:data];
    }
    
    return request;
}

- (void)setNetworkLoaderVisible:(BOOL)visible {
    static int visibleNumber = 0;
    
    if (visible) {
        visibleNumber++;
    } else {
        visibleNumber--;
    }
    
    [[UIApplication sharedApplication] setNetworkActivityIndicatorVisible:(visibleNumber > 0)];
}

@end
